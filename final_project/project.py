import math
import sys
from tabulate import tabulate

# Physical constant: Speed of light (m/s)
C = 299792458.0

# Shielding materials linear attenuation coefficient (cm^-1)
MATERIALS = {
    "Lead": 0.772,
    "Tungsten": 1.251,
    "Steel": 0.471,
    "Concrete": 0.149,
    "Water": 0.071,
}

# Isotopes half-life in years
ISOTOPES = {
    "Cobalt-60": 5.27,
    "Cesium-137": 30.17,
    "Strontium-90": 28.80,
    "Uranium-235": 704000000.0,
}


def main():
    """Main function to launch Web App or CLI menu."""
    if "streamlit" in sys.modules:
        run_web_app()
    else:
        run_cli()


def calculate_decay(initial, half_life, time):
    """
    Calculates remaining radioactive amount using N(t) = N0 * (0.5)^(t / T_half).
    """
    if initial < 0 or time < 0:
        raise ValueError("Initial amount and time cannot be negative.")
    if half_life <= 0:
        raise ValueError("Half-life must be greater than zero.")

    return round(initial * (0.5 ** (time / half_life)), 4)


def calculate_shielding(initial_dose, mu, thickness):
    """
    Calculates transmitted radiation dose using Beer-Lambert Law: I = I0 * e^(-mu * x).
    """
    if initial_dose < 0 or thickness < 0:
        raise ValueError("Dose and thickness cannot be negative.")
    if mu <= 0:
        raise ValueError("Attenuation coefficient must be greater than zero.")

    return round(initial_dose * math.exp(-mu * thickness), 4)


def calculate_reactivity(k_eff):
    """
    Calculates reactor reactivity rho = (k_eff - 1) / k_eff and reactor state.
    """
    if k_eff <= 0:
        raise ValueError("k_eff must be greater than zero.")

    rho = round((k_eff - 1) / k_eff, 5)

    if math.isclose(k_eff, 1.0, abs_tol=1e-4):
        state = "CRITICAL"
    elif k_eff < 1.0:
        state = "SUBCRITICAL"
    else:
        state = "SUPERCRITICAL"

    return {"rho": rho, "state": state}


def calculate_energy(mass_grams):
    """
    Calculates nuclear energy in Megajoules (MJ) using Einstein's E = m * c^2.
    """
    if mass_grams < 0:
        raise ValueError("Mass cannot be negative.")

    mass_kg = mass_grams / 1000.0
    joules = mass_kg * (C ** 2)
    megajoules = joules / 1e6
    return round(megajoules, 2)


def run_web_app():
    """Runs the clean Streamlit Web Application."""
    import streamlit as st

    st.set_page_config(page_title="NucCalc CS50P",)
    st.title("NucCalc: Nuclear Engineering Calculator")
    st.write("All-in-One Nuclear Physics & Engineering Web App for CS50P.")

    tab1, tab2, tab3, tab4 = st.tabs([
        "1. Decay",
        "2. Shielding",
        "3. Reactor",
        "4. Energy (E=mc²)"
    ])

    with tab1:
        st.subheader("Radioactive Decay Calculator")
        isotope = st.selectbox("Select Isotope", list(ISOTOPES.keys()))
        initial = st.number_input("Initial Mass (g)", min_value=0.0, value=100.0)
        half_life = st.number_input("Half-Life (years)", min_value=0.01, value=ISOTOPES[isotope])
        time = st.number_input("Time Elapsed (years)", min_value=0.0, value=5.27)

        remaining = calculate_decay(initial, half_life, time)
        st.success(f"Remaining Mass: **{remaining} g**")

    with tab2:
        st.subheader("Radiation Shielding Calculator")
        material = st.selectbox("Select Material", list(MATERIALS.keys()))
        dose = st.number_input("Initial Dose Rate (mSv/h)", min_value=0.0, value=100.0)
        thickness = st.number_input("Shield Thickness (cm)", min_value=0.0, value=10.0)

        transmitted = calculate_shielding(dose, MATERIALS[material], thickness)
        st.info(f"Transmitted Dose Rate: **{transmitted} mSv/h**")
        if transmitted <= 0.02:
            st.success("Safety Status: SAFE (<= 0.02 mSv/h)")
        else:
            st.warning("Safety Status: CAUTION / DANGER (> 0.02 mSv/h)")

    with tab3:
        st.subheader("Reactor Criticality & Reactivity")
        k_eff = st.number_input("Neutron Multiplication Factor (k_eff)", min_value=0.1, value=1.00, step=0.01)

        result = calculate_reactivity(k_eff)
        st.metric("Reactor State", result["state"])
        st.metric("Reactivity (ρ)", result["rho"])

    with tab4:
        st.subheader("Mass-Energy Equivalence (E = mc²)")
        mass = st.number_input("Mass Defect (grams)", min_value=0.0, value=1.0)

        energy_mj = calculate_energy(mass)
        st.success(f"Released Energy: **{energy_mj:,.2f} Megajoules (MJ)**")


def run_cli():
    """Runs the clean terminal interface."""
    print("\n=== NucCalc: Nuclear Engineering Calculator ===")
    print("1. Radioactive Decay Calculator")
    print("2. Radiation Shielding Calculator")
    print("3. Reactor Criticality Calculator")
    print("4. Mass-Energy (E=mc^2) Calculator")
    print("5. Exit")

    while True:
        choice = input("\nChoose an option (1-5): ").strip()

        try:
            if choice == "1":
                n0 = float(input("Initial Mass (g): "))
                hl = float(input("Half-Life (years): "))
                t = float(input("Time Elapsed (years): "))
                ans = calculate_decay(n0, hl, t)
                print(tabulate([["Remaining Mass (g)", ans]], headers=["Result", "Value"], tablefmt="grid"))

            elif choice == "2":
                print("Materials:", ", ".join(MATERIALS.keys()))
                mat = input("Material Name: ").strip().title()
                if mat not in MATERIALS:
                    print("Invalid material.")
                    continue
                i0 = float(input("Initial Dose (mSv/h): "))
                x = float(input("Thickness (cm): "))
                ans = calculate_shielding(i0, MATERIALS[mat], x)
                print(tabulate([["Transmitted Dose (mSv/h)", ans]], headers=["Result", "Value"], tablefmt="grid"))

            elif choice == "3":
                k = float(input("Enter k_eff (e.g., 1.0): "))
                res = calculate_reactivity(k)
                table = [["Reactor State", res["state"]], ["Reactivity (rho)", res["rho"]]]
                print(tabulate(table, headers=["Parameter", "Value"], tablefmt="grid"))

            elif choice == "4":
                m = float(input("Enter Mass (grams): "))
                ans = calculate_energy(m)
                print(tabulate([["Energy Released (MJ)", f"{ans:,.2f}"]], headers=["Result", "Value"], tablefmt="grid"))

            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1 to 5.")

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
