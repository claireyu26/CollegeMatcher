---

# CollegeMatcher

CollegeMatcher is an AI-driven mobile application designed to support high school students navigating the college application process. The platform provides structured university information, campus imagery, and personalized university recommendations generated from user input. The project focuses on accessibility, clarity, and reducing barriers to college exploration, particularly for students who lack access to in-person campus visits or individualized counseling.

This repository contains the source code for the frontend, backend data pipelines, and supporting scripts used to power the application.

---

## Project Overview

Many students feel overwhelmed by the college application process due to limited guidance, information overload, or lack of access to campus resources. CollegeMatcher addresses this by combining:

* Curated university data collected via web scraping and APIs
* Visual representations of campuses using building-level images
* A recommendation system powered by an OpenAI language model
* A mobile-first interface built with Flutter

Rather than replacing human counselors, the application is intended as an accessible starting point for exploration and reflection.

---

## System Architecture

CollegeMatcher uses a multi-layer architecture:

### Backend (Python)

* Web scraping scripts extract university descriptions, building names, and image sources
* Google Maps API is used to retrieve:

  * University addresses
  * Nearby places
  * Building-level photo URLs
* Data is cleaned, validated, and structured before being stored
* A Firebase database serves as the bridge between backend scripts and the frontend application

### Frontend (Flutter / Dart)

* Displays university lists, detailed school pages, and building image galleries
* Provides search functionality across all universities
* Hosts the recommendations interface where users input academic and personal preferences
* Integrates directly with the OpenAI API to generate recommendations in real time

### AI Recommendations

* Uses an OpenAI general-purpose language model (via API)
* Combines:

  * User-entered academic data (grades, activities, awards)
  * School preferences (location, type, prestige range)
* Returns a list of up to 20 recommended universities with brief justifications
* Recommendations are generated on demand and are not stored locally or server-side

---

## Tech Stack

**Frontend**

* Flutter
* Dart

**Backend**

* Python
* Web scraping (custom scripts)
* Google Maps API

**AI**

* OpenAI API (ChatGPT)

**Database**

* Firebase (used for structured storage of scraped and API-derived data)

---

## Repository Structure

```
CollegeMatcher/
├── Dart/                 # Flutter frontend application
├── Python/               # Backend scripts (web scraping, API integration)
├── metadata/             # Supporting project metadata
├── CMakeLists.txt
├── .gitignore
└── README.md
```

Some directories contain experimental or supporting code used during development.

---

## Key Features

* Structured university profiles with descriptions and location data
* Campus visualization through building-level image galleries
* Searchable database of universities
* AI-powered recommendation page driven by user input
* Real-time generation of results without persistent storage of personal data

---

## Data and Accuracy Considerations

* University data is gathered from a combination of web scraping and third-party APIs
* Some scraped data required manual verification and correction
* Google Maps API data may change over time and requires periodic re-fetching
* AI-generated recommendations may vary between runs due to the probabilistic nature of large language models

The project treats AI output as advisory rather than authoritative.

---

## Known Limitations

* Recommendation consistency varies due to model behavior
* Some universities may have incomplete or manually patched data
* Firebase structure evolved during development and may not be optimal for scale
* The system does not currently support user accounts or saved histories
* 360-degree virtual campus tours were planned but not implemented due to API restrictions

These limitations are documented intentionally and inform future development goals.

---

## Future Work

Planned and proposed improvements include:

* More structured recommendation constraints (safety/match/reach categorization)
* Program- and major-specific filtering
* Cost, financial aid, and acceptance rate integration
* Evaluation of alternative AI models
* Improved database schema and update pipelines
* Enhanced UI accessibility and navigation
* Optional user accounts and saved preferences

---

## Ethics and Privacy

* The application does not collect personally identifiable information
* User input is sent to the OpenAI API only for real-time response generation
* No user data is stored persistently
* AI bias and hallucination risks are acknowledged and actively considered in prompt design

---

## License

This project is open source. See the repository license for details.

---

* Help you write a **methods.md** or **architecture.md** for reviewers or judges
