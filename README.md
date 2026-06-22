# 📊 Marks to GPA Converter

A Python program that converts marks into letter grades and calculates **GPA** and **CGPA** — supporting grading scales out of **80** or **60** marks. Designed for students and educators who want a quick, reliable way to track academic performance.

---

## ✨ Features

- 🔢 **Dual grading scales** — supports marks out of 80 or 60
- 🎓 **Letter grade conversion** — automatically maps marks to grades (A+, A, B+, B, C, D, F, etc.)
- 📚 **Multi-subject entry** — enter marks and credit hours for multiple subjects in one session
- 📈 **Semester GPA calculation** — computes weighted GPA across all entered subjects
- 🔄 **CGPA computation** — optionally factors in previous GPA and credit hours for a cumulative result
- 🖥️ **Simple CLI interface** — clean, interactive command-line experience

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your machine

### Installation

```bash
git clone https://github.com/your-username/marks-to-gpa-converter.git
cd marks-to-gpa-converter
```

### Run the Program

```bash
python gpa_converter.py
```

---

## 🖥️ Usage

1. **Choose your grading scale** — select marks out of `80` or `60`
2. **Enter subject details** — provide marks and credit hours for each subject
3. **View results** — the program displays the letter grade and grade points per subject
4. **Get semester GPA** — calculated automatically after all subjects are entered
5. **Calculate CGPA (optional)** — input your previous CGPA and total credit hours to get your cumulative GPA

---

## 📋 Grading Scale

### Out of 80 Marks

| Marks Range | Letter Grade | Grade Points |
|-------------|--------------|--------------|
| 72 – 80     | A+           | 4.00         |
| 64 – 71     | A            | 4.00         |
| 60 – 63     | B+           | 3.50         |
| 56 – 59     | B            | 3.00         |
| 52 – 55     | C+           | 2.50         |
| 48 – 51     | C            | 2.00         |
| 44 – 47     | D+           | 1.50         |
| 40 – 43     | D            | 1.00         |
| Below 40    | F            | 0.00         |

### Out of 60 Marks

| Marks Range | Letter Grade | Grade Points |
|-------------|--------------|--------------|
| 54 – 60     | A+           | 4.00         |
| 48 – 53     | A            | 4.00         |
| 45 – 47     | B+           | 3.50         |
| 42 – 44     | B            | 3.00         |
| 39 – 41     | C+           | 2.50         |
| 36 – 38     | C            | 2.00         |
| 33 – 35     | D+           | 1.50         |
| 30 – 32     | D            | 1.00         |
| Below 30    | F            | 0.00         |

> ⚠️ *Grading scales may vary by institution. Adjust the ranges in the source code if needed.*

---

## 📂 Project Structure

```
marks-to-gpa-converter/
│
├── gpa_converter.py   # Main program file
└── README.md          # Project documentation
```

---

## 🛠️ How GPA is Calculated

**GPA Formula:**

```
GPA = Σ (Grade Points × Credit Hours) / Σ Credit Hours
```

**CGPA Formula:**

```
CGPA = (Previous GPA × Previous Credit Hours + Current GPA × Current Credit Hours)
       ÷ (Previous Credit Hours + Current Credit Hours)
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for:

- Additional grading scale support
- GUI version
- Export results to PDF/Excel

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Roman Ahmad Khan**  
BS Computer Science — GC University Faisalabad  

🔗 [linkedin.com/in/roman-ahmad-kh](https://linkedin.com/in/roman-ahmad-kh)
