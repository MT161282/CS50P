# NucCalc: Nuclear Engineering Calculator

#### Video Demo: https://youtu.be/mEHzsSiluWg

#### Description:

**NucCalc** is a comprehensive Python application designed to perform essential nuclear physics and reactor engineering calculations. Created as my final project for Harvard University's **CS50's Introduction to Programming with Python (CS50P)**, this project combines a modern web interface built with **Streamlit** alongside an interactive command-line interface (CLI) formatted using **tabulate**.

As an aspiring nuclear engineering student, my goal was to develop a reliable computational tool where students, technicians, and researchers can quickly model radioactive decay, calculate radiation shielding thickness, determine reactor core criticality, and evaluate relativistic mass-energy conversion without redundant manual calculations.

---

### Key Features & Functions

The project architecture strictly follows CS50P specifications. All core engineering algorithms are located at the root level of `project.py` alongside `main()`, making them completely decoupled from the UI and readily testable:

1. **`calculate_decay(initial, half_life, time)`**:
   Computes the remaining mass of a radioactive isotope after an elapsed time period using the exponential half-life decay formula:
   $$N(t) = N_0 \times \left(\frac{1}{2}\right)^{\frac{t}{T_{1/2}}}$$
   - **Parameters:** `initial` (float, $N_0 > 0$), `half_life` (float, $T_{1/2} > 0$), and `time` (float, $t \ge 0$).
   - **Returns:** The remaining radioactive quantity as a floating-point number.
   - **Exception Handling:** Raises a `ValueError` if either `initial` or `half_life` is non-positive, or if `time` is negative.

2. **`calculate_shielding(initial_dose, mu, thickness)`**:
   Determines the transmitted gamma radiation dose rate through protective shielding material according to the Beer-Lambert attenuation law:
   $$I = I_0 \times e^{-\mu x}$$
   - **Parameters:** `initial_dose` (float, $I_0 > 0$), `mu` (linear attenuation coefficient $\mu > 0$ in $\text{cm}^{-1}$), and `thickness` (material thickness $x \ge 0$ in $\text{cm}$).
   - **Returns:** A dictionary containing the transmitted intensity (`transmitted`), the percentage of radiation blocked (`attenuation_pct`), and a safety classification (`status`: `SAFE` if transmitted dose $\le 0.02\text{ mSv/h}$, otherwise `UNSAFE - SHIELDING REQUIRED`).
   - **Exception Handling:** Raises a `ValueError` for invalid negative or zero parameters.

3. **`calculate_reactivity(k_eff)`**:
   Evaluates neutron population balance and state of a nuclear reactor core from its effective neutron multiplication factor ($k_{\text{eff}}$):
   $$\rho = \frac{k_{\text{eff}} - 1}{k_{\text{eff}}}$$
   - **Parameters:** `k_eff` (float, $k_{\text{eff}} > 0$).
   - **Returns:** A dictionary containing numerical reactivity (`rho`) and core status (`state`: `CRITICAL` when $k_{\text{eff}} = 1.0$, `SUPERCRITICAL` when $k_{\text{eff}} > 1.0$, or `SUBCRITICAL` when $k_{\text{eff}} < 1.0$).
   - **Exception Handling:** Raises a `ValueError` if $k_{\text{eff}} \le 0$.

4. **`calculate_energy(mass_grams)`**:
   Calculates the energy released during mass-defect conversion via Einstein's mass-energy equivalence equation ($E = mc^2$):
   - **Parameters:** `mass_grams` (float, $m \ge 0$).
   - **Returns:** Total energy yield released in Megajoules ($\text{MJ}$).
   - **Exception Handling:** Raises a `ValueError` if mass is strictly negative.

---

### File Structure & Modules

- **`project.py`**: The primary program containing `main()`, the four custom calculation functions, the interactive CLI execution loop (`run_cli`), and the Streamlit web dashboard (`run_web_app`).
- **`test_project.py`**: The automated test suite containing unit tests for all four mathematical functions using `pytest`. It verifies expected return values, edge cases, and exception handling (`pytest.raises(ValueError)`).
- **`requirements.txt`**: Lists all third-party dependencies required to execute the program (`tabulate`, `streamlit`, and `pytest`).
- **`shielding_materials.csv`**: Reference dataset containing standard linear attenuation coefficients ($\mu$) for shielding materials such as Lead, Tungsten, Steel, Concrete, and Water.
- **`README.md`**: Complete markdown documentation explaining project motivation, mathematical models, architecture, and instructions.

---

### Design Choices

During development, I prioritized modularity and clean separation of concerns. While CS50P primarily benchmarks standard terminal scripts, modern scientific work benefits from intuitive dashboards. Therefore, `project.py` was architected to seamlessly support dual runtime modes:
1. **Interactive CLI Mode:** Executing `python project.py` presents an accessible, menu-driven command-line loop that outputs results in clean, formatted tables using `tabulate`.
2. **Streamlit Web Dashboard:** Running `streamlit run project.py` launches a responsive browser application equipped with sliders, isotope selectors, and visual metrics.

By keeping the calculation algorithms independent of UI logic, the application remains fully testable through automated test pipelines while delivering an executive portfolio deliverable.

---

### How to Run

1. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
