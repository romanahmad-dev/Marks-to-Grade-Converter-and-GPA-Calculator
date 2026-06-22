# ðŸ“Š Marks to GPA Converter

A Python program that converts marks into letter grades and calculates **GPA** and **CGPA** â€” supporting grading scales out of **80** or **60** marks. Designed for students and educators who want a quick, reliable way to track academic performance.

---

## âœ¨ Features

- ðŸ”¢ **Dual grading scales** â€” supports marks out of 80 or 60
- ðŸŽ“ **Letter grade conversion** â€” automatically maps marks to grades (A+, A, B+, B, C, D, F, etc.)
- ðŸ“š **Multi-subject entry** â€” enter marks and credit hours for multiple subjects in one session
- ðŸ“ˆ **Semester GPA calculation** â€” computes weighted GPA across all entered subjects
- ðŸ”„ **CGPA computation** â€” optionally factors in previous GPA and credit hours for a cumulative result
- ðŸ–¥ï¸ **Simple CLI interface** â€” clean, interactive command-line experience

---

## ðŸš€ Getting Started

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

## ðŸ–¥ï¸ Usage

1. **Choose your grading scale** â€” select marks out of `80` or `60`
2. **Enter subject details** â€” provide marks and credit hours for each subject
3. **View results** â€” the program displays the letter grade and grade points per subject
4. **Get semester GPA** â€” calculated automatically after all subjects are entered
5. **Calculate CGPA (optional)** â€” input your previous CGPA and total credit hours to get your cumulative GPA

---

## ðŸ“‹ Grading Scale

### Out of 80 Marks

| Marks Range | Letter Grade | Grade Points |
|-------------|--------------|--------------|
| 72 â€“ 80     | A+           | 4.00         |
| 64 â€“ 71     | A            | 4.00         |
| 60 â€“ 63     | B+           | 3.50         |
| 56 â€“ 59     | B            | 3.00         |
| 52 â€“ 55     | C+           | 2.50         |
| 48 â€“ 51     | C            | 2.00         |
| 44 â€“ 47     | D+           | 1.50         |
| 40 â€“ 43     | D            | 1.00         |
| Below 40    | F            | 0.00         |

### Out of 60 Marks

| Marks Range | Letter Grade | Grade Points |
|-------------|--------------|--------------|
| 54 â€“ 60     | A+           | 4.00         |
| 48 â€“ 53     | A            | 4.00         |
| 45 â€“ 47     | B+           | 3.50         |
| 42 â€“ 44     | B            | 3.00         |
| 39 â€“ 41     | C+           | 2.50         |
| 36 â€“ 38     | C            | 2.00         |
| 33 â€“ 35     | D+           | 1.50         |
| 30 â€“ 32     | D            | 1.00         |
| Below 30    | F            | 0.00         |

> âš ï¸ *Grading scales may vary by institution. Adjust the ranges in the source code if needed.*

---

## ðŸ“‚ Project Structure

```
marks-to-gpa-converter/
â”‚
â”œâ”€â”€ gpa_converter.py   # Main program file
â””â”€â”€ README.md          # Project documentation
```

---

## ðŸ› ï¸ How GPA is Calculated

**GPA Formula:**

```
GPA = Î£ (Grade Points Ã— Credit Hours) / Î£ Credit Hours
```

**CGPA Formula:**

```
CGPA = (Previous GPA Ã— Previous Credit Hours + Current GPA Ã— Current Credit Hours)
       Ã· (Previous Credit Hours + Current Credit Hours)
```

---

## ðŸ¤ Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for:

- Additional grading scale support
- GUI version
- Export results to PDF/Excel

---

## ðŸ“„ License

This project is open-source and available under the [MIT License](LICENSE).

---

## ðŸ‘¤ Author

**Roman Ahmad Khan**  
BS Computer Science â€” GC University Faisalabad    
ðŸ”— [linkedin.com/in/roman-ahmad-kh](https://linkedin.com/in/roman-ahmad-kh)
