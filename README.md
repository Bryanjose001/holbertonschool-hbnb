# HBnB Evolution – Technical Documentation

## 📘 Overview

This repository contains the technical documentation for the **HBnB Evolution** project – a simplified AirBnB-like application. The goal of this documentation is to provide a clear and structured foundation for the system's design, covering architecture, business logic, and key interactions.

---

## 📌 Objective

The main objective of this phase is to design and document:

- System architecture
- Business entities and relationships
- API interactions
- Data persistence structure

This documentation will guide the development process in the upcoming stages.

---

## 🛠️ Documentation Components

### 1. **Architecture Design**
- A high-level package diagram representing the three-layered architecture:
  - Presentation Layer
  - Business Logic Layer
  - Persistence Layer
- Communication modeled using the **Facade Pattern**

### 2. **Class Diagrams**
- Detailed UML class diagrams for:
  - User
  - Place
  - Review
  - Amenity
- Includes attributes, methods, and relationships

### 3. **Sequence Diagrams**
- Sequence diagrams for four main API interactions:
  - User registration
  - Place creation
  - Review submission
  - Fetching list of places

### 4. **Explanatory Notes**
- Written descriptions accompany each diagram
- Explanation of design decisions and business rule implementations

---

## 📋 Business Rules Implemented

- User roles (regular/admin), registration, profile update, and deletion
- Place creation with amenities, location, and pricing
- Reviews with rating and comment linked to users and places
- Amenity management with linking to places
- Unique IDs and audit timestamps for all entities

---

## 📎 Tools & Notation

- All diagrams follow standard **UML notation**
- Created using [Tool Name – e.g., Lucidchart, Draw.io, etc.] *(Add tool if applicable)*

---

## ✅ Output

The complete documentation serves as a blueprint for the implementation phase and ensures all stakeholders understand the system's structure and logic.

---


