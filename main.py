#!/usr/bin/env python3
"""
Medicinal Herbal App
A comprehensive application for browsing and learning about medicinal herbs.
"""

import json
from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime
import os


@dataclass
class Herb:
    """Data class representing a medicinal herb."""
    name: str
    scientific_name: str
    family: str
    description: str
    benefits: List[str]
    active_compounds: List[str]
    preparation_methods: Dict[str, str]
    dosage: str
    contraindications: List[str]
    interactions: List[str]
    parts_used: List[str]
    traditional_uses: List[str]


class HerbalDatabase:
    """Database manager for medicinal herbs."""

    def __init__(self, db_file: str = "herbs_database.json"):
        self.db_file = db_file
        self.herbs: Dict[str, Herb] = {}
        self.load_database()

    def load_database(self) -> None:
        """Load herbs from JSON database."""
        if os.path.exists(self.db_file):
            with open(self.db_file, 'r') as f:
                data = json.load(f)
                for herb_name, herb_data in data.items():
                    self.herbs[herb_name.lower()] = Herb(**herb_data)
        else:
            self._initialize_default_herbs()
            self.save_database()

    def _initialize_default_herbs(self) -> None:
        """Initialize database with common medicinal herbs."""
        default_herbs = {
            "chamomile": {
                "name": "Chamomile",
                "scientific_name": "Matricaria chamomilla",
                "family": "Asteraceae",
                "description": "A gentle flowering herb known for its calming properties.",
                "benefits": ["Sleep aid", "Digestive support", "Stress relief", "Anti-inflammatory"],
                "active_compounds": ["Apigenin", "Bisabolol", "Chamazulene"],
                "preparation_methods": {
                    "tea": "Steep 1-2 teaspoons dried flowers in hot water for 5-10 minutes",
                    "tincture": "Take 1 teaspoon in water, 2-3 times daily"
                },
                "dosage": "1-4 grams daily",
                "contraindications": ["Pregnancy (consult doctor)", "Allergy to Asteraceae family"],
                "interactions": ["Sedatives", "Anticoagulants"],
                "parts_used": ["Flowers"],
                "traditional_uses": ["Insomnia", "Anxiety", "Digestive upset", "Inflammation"]
            },
            "ginger": {
                "name": "Ginger",
                "scientific_name": "Zingiber officinale",
                "family": "Zingiberaceae",
                "description": "A warming spice with powerful anti-inflammatory and digestive properties.",
                "benefits": ["Nausea relief", "Digestive support", "Anti-inflammatory", "Pain relief"],
                "active_compounds": ["Gingerol", "Shogaol", "Zingerone"],
                "preparation_methods": {
                    "tea": "Simmer 1-2 inch fresh root in water for 10-20 minutes",
                    "decoction": "Boil for 10-20 minutes, strain and drink",
                    "fresh": "Add to cooking or eat raw in small amounts"
                },
                "dosage": "1-2 grams dried or 10-20 grams fresh daily",
                "contraindications": ["Gallstones (consult doctor)", "Blood clotting disorders"],
                "interactions": ["Anticoagulants", "Antiplatelet drugs"],
                "parts_used": ["Rhizome"],
                "traditional_uses": ["Nausea", "Motion sickness", "Inflammation", "Arthritis"]
            },
            "turmeric": {
                "name": "Turmeric",
                "scientific_name": "Curcuma longa",
                "family": "Zingiberaceae",
                "description": "Golden spice containing curcumin, a powerful antioxidant and anti-inflammatory.",
                "benefits": ["Anti-inflammatory", "Antioxidant", "Joint support", "Digestive health"],
                "active_compounds": ["Curcumin", "Demethoxycurcumin", "Bisdemethoxycurcumin"],
                "preparation_methods": {
                    "golden milk": "Mix with milk, honey, and black pepper",
                    "tea": "Steep powder in hot water with milk",
                    "cooking": "Add to curries, rice, and soups"
                },
                "dosage": "0.5-1 gram daily (with black pepper for absorption)",
                "contraindications": ["Pregnancy", "Gallstones", "Blood clotting disorders"],
                "interactions": ["Blood thinners", "Diabetes medications"],
                "parts_used": ["Rhizome"],
                "traditional_uses": ["Inflammation", "Arthritis", "Digestion", "Detoxification"]
            },
            "peppermint": {
                "name": "Peppermint",
                "scientific_name": "Mentha piperita",
                "family": "Lamiaceae",
                "description": "Refreshing herb known for digestive comfort and mental clarity.",
                "benefits": ["Digestive aid", "Headache relief", "Respiratory support", "Mental clarity"],
                "active_compounds": ["Menthol", "Menthone", "Limonene"],
                "preparation_methods": {
                    "tea": "Steep fresh or dried leaves for 5-10 minutes",
                    "infusion": "Pour hot water over leaves and let steep",
                    "inhalation": "Breathe in steam from hot water"
                },
                "dosage": "1-3 cups of tea daily",
                "contraindications": ["GERD (can worsen)", "Gallstones"],
                "interactions": ["Calcium channel blockers"],
                "parts_used": ["Leaves"],
                "traditional_uses": ["Digestive upset", "Bloating", "Migraines", "Respiratory congestion"]
            },
            "echinacea": {
                "name": "Echinacea",
                "scientific_name": "Echinacea purpurea",
                "family": "Asteraceae",
                "description": "Purple coneflower known for supporting immune system function.",
                "benefits": ["Immune support", "Cold duration reduction", "Wound healing", "Anti-inflammatory"],
                "active_compounds": ["Alkamides", "Polysaccharides", "Caffeic acid derivatives"],
                "preparation_methods": {
                    "tincture": "Take 1 teaspoon 2-3 times daily",
                    "tea": "Steep 1-2 teaspoons dried root/flowers for 10 minutes",
                    "supplement": "Follow package directions"
                },
                "dosage": "300-500 mg three times daily",
                "contraindications": ["Autoimmune conditions (consult doctor)", "Allergies to Asteraceae"],
                "interactions": ["Immunosuppressants"],
                "parts_used": ["Roots", "Flowers", "Leaves"],
                "traditional_uses": ["Common cold", "Flu", "Immune support", "Wound healing"]
            }
        }

        for herb_name, herb_data in default_herbs.items():
            self.herbs[herb_name] = Herb(**herb_data)

    def save_database(self) -> None:
        """Save herbs to JSON database."""
        data = {}
        for herb_name, herb in self.herbs.items():
            data[herb_name] = {
                "name": herb.name,
                "scientific_name": herb.scientific_name,
                "family": herb.family,
                "description": herb.description,
                "benefits": herb.benefits,
                "active_compounds": herb.active_compounds,
                "preparation_methods": herb.preparation_methods,
                "dosage": herb.dosage,
                "contraindications": herb.contraindications,
                "interactions": herb.interactions,
                "parts_used": herb.parts_used,
                "traditional_uses": herb.traditional_uses
            }
        with open(self.db_file, 'w') as f:
            json.dump(data, f, indent=2)

    def search_herb(self, query: str) -> Optional[Herb]:
        """Search for a herb by name."""
        query = query.lower().strip()
        return self.herbs.get(query)

    def search_by_benefit(self, benefit: str) -> List[Herb]:
        """Search herbs by health benefit."""
        benefit_lower = benefit.lower()
        results = []
        for herb in self.herbs.values():
            if any(benefit_lower in b.lower() for b in herb.benefits):
                results.append(herb)
        return results

    def search_by_family(self, family: str) -> List[Herb]:
        """Search herbs by plant family."""
        family_lower = family.lower()
        return [herb for herb in self.herbs.values() 
                if family_lower in herb.family.lower()]

    def list_all_herbs(self) -> List[str]:
        """Get list of all available herbs."""
        return sorted([herb.name for herb in self.herbs.values()])

    def add_herb(self, herb: Herb) -> None:
        """Add a new herb to the database."""
        self.herbs[herb.name.lower()] = herb
        self.save_database()


class HerbalApp:
    """Main application class for the Medicinal Herbal App."""

    def __init__(self):
        self.db = HerbalDatabase()
        self.favorites: List[str] = []
        self.load_favorites()

    def load_favorites(self) -> None:
        """Load favorite herbs from file."""
        if os.path.exists("favorites.json"):
            with open("favorites.json", 'r') as f:
                self.favorites = json.load(f)

    def save_favorites(self) -> None:
        """Save favorite herbs to file."""
        with open("favorites.json", 'w') as f:
            json.dump(self.favorites, f, indent=2)

    def display_medical_disclaimer(self) -> str:
        """Display medical disclaimer before herb information."""
        disclaimer = [
            "\n" + "!"*60,
            "⚠️  IMPORTANT MEDICAL DISCLAIMER ⚠️",
            "!"*60,
            "\nThis application is for EDUCATIONAL PURPOSES ONLY.",
            "It is NOT a substitute for professional medical advice.",
            "\n✓ CONSULT A DOCTOR OR HEALTHCARE PROFESSIONAL BEFORE:",
            "  • Using any herbal remedies",
            "  • Starting any herbal supplement",
            "  • Combining herbs with prescription medications",
            "  • Using herbs if you have existing medical conditions",
            "  • Using herbs during pregnancy or breastfeeding",
            "\n✓ Herbs can have serious interactions with medications",
            "✓ Herbs may cause allergic reactions or side effects",
            "✓ Dosages matter - more is not always better",
            "✓ Quality and safety vary by source and preparation",
            "\nDo NOT rely on this app for medical decisions.",
            "Always seek professional medical guidance.",
            "!"*60 + "\n",
        ]
        return "\n".join(disclaimer)

    def display_herb_details(self, herb: Herb) -> str:
        """Format herb information for display with warnings."""
        output = []
        
        # Add medical disclaimer at top
        output.append(self.display_medical_disclaimer())
        
        output.append(f"\n{'='*60}")
        output.append(f"HERB: {herb.name}")
        output.append(f"{'='*60}")
        output.append(f"Scientific Name: {herb.scientific_name}")
        output.append(f"Family: {herb.family}")
        output.append(f"\nDescription:\n{herb.description}")
        
        output.append(f"\nBenefits:")
        for benefit in herb.benefits:
            output.append(f"  • {benefit}")
        
        output.append(f"\nActive Compounds:")
        for compound in herb.active_compounds:
            output.append(f"  • {compound}")
        
        output.append(f"\nParts Used:")
        for part in herb.parts_used:
            output.append(f"  • {part}")
        
        output.append(f"\nTraditional Uses:")
        for use in herb.traditional_uses:
            output.append(f"  • {use}")
        
        output.append(f"\nPreparation Methods:")
        for method, instructions in herb.preparation_methods.items():
            output.append(f"  {method.upper()}:")
            output.append(f"    {instructions}")
        
        output.append(f"\nDosage: {herb.dosage}")
        
        # Prominent warnings section
        output.append(f"\n{'!'*60}")
        output.append("⚠️  CONTRAINDICATIONS & HEALTH WARNINGS ⚠️")
        output.append(f"{'!'*60}")
        output.append("\nDO NOT USE if you have:")
        for contra in herb.contraindications:
            output.append(f"  ⚠️  {contra}")
        
        output.append(f"\n{'!'*60}")
        output.append("⚠️  MEDICATION & HERB INTERACTIONS ⚠️")
        output.append(f"{'!'*60}")
        output.append(f"\nThis herb does NOT work well with:")
        for interaction in herb.interactions:
            output.append(f"  ⚠️  {interaction}")
        
        output.append(f"\nIMPORTANT: If you take ANY of these medications,")
        output.append(f"CONSULT YOUR DOCTOR before using {herb.name}.")
        
        # Final disclaimer
        output.append(f"\n{'!'*60}")
        output.append("⚠️  BEFORE YOU USE THIS HERB ⚠️")
        output.append(f"{'!'*60}")
        output.append("\n✓ Tell your doctor about ALL herbs you plan to use")
        output.append("✓ Check for allergies or sensitivities first")
        output.append("✓ Start with small amounts to test tolerance")
        output.append("✓ Buy from reputable, quality sources only")
        output.append("✓ Stop use if you experience any adverse effects")
        output.append("✓ Never replace medical treatment with herbs alone")
        output.append("\nYour health and safety are paramount.")
        output.append("When in doubt, ask a healthcare professional.")
        
        output.append(f"\n{'='*60}\n")
        
        return "\n".join(output)

    def show_menu(self) -> None:
        """Display main menu."""
        print("\n" + "="*60)
        print("MEDICINAL HERBAL APP")
        print("="*60)
        print("1. Search for a specific herb")
        print("2. Browse all herbs")
        print("3. Search by health benefit")
        print("4. Search by plant family")
        print("5. View favorites")
        print("6. Add to favorites")
        print("7. Exit")
        print("="*60)

    def run(self) -> None:
        """Run the application."""
        while True:
            self.show_menu()
            choice = input("\nEnter your choice (1-7): ").strip()
            
            if choice == "1":
                self.search_herb_by_name()
            elif choice == "2":
                self.browse_all_herbs()
            elif choice == "3":
                self.search_by_benefit()
            elif choice == "4":
                self.search_by_family()
            elif choice == "5":
                self.view_favorites()
            elif choice == "6":
                self.add_to_favorites()
            elif choice == "7":
                print("\nThank you for using Medicinal Herbal App.")
                print("Please consult healthcare professionals for medical advice.")
                print("Stay healthy and safe!")
                break
            else:
                print("\nInvalid choice. Please try again.")

    def search_herb_by_name(self) -> None:
        """Search for herb by name."""
        query = input("\nEnter herb name: ").strip()
        herb = self.db.search_herb(query)
        
        if herb:
            print(self.display_herb_details(herb))
        else:
            print(f"\nHerb '{query}' not found in database.")
            print("Available herbs:", ", ".join(self.db.list_all_herbs()))

    def browse_all_herbs(self) -> None:
        """Display all available herbs."""
        herbs = self.db.list_all_herbs()
        print("\n" + "="*60)
        print("AVAILABLE HERBS")
        print("="*60)
        for i, herb_name in enumerate(herbs, 1):
            print(f"{i}. {herb_name}")
        
        try:
            choice = int(input("\nSelect herb number (0 to go back): "))
            if 1 <= choice <= len(herbs):
                herb = self.db.search_herb(herbs[choice - 1])
                print(self.display_herb_details(herb))
        except ValueError:
            print("Invalid input.")

    def search_by_benefit(self) -> None:
        """Search herbs by health benefit."""
        print("\nCommon benefits:")
        benefits = set()
        for herb in self.db.herbs.values():
            for benefit in herb.benefits:
                benefits.add(benefit)
        
        for i, benefit in enumerate(sorted(benefits), 1):
            print(f"{i}. {benefit}")
        
        query = input("\nEnter benefit to search (or type custom): ").strip()
        results = self.db.search_by_benefit(query)
        
        if results:
            print(f"\n✓ Found {len(results)} herb(s) for '{query}':")
            for herb in results:
                print(f"\n  • {herb.name} - {herb.scientific_name}")
                for benefit in herb.benefits:
                    if query.lower() in benefit.lower():
                        print(f"    ✓ {benefit}")
            
            view_details = input("\nView full details of any herb? Enter name or 'n': ").strip()
            if view_details.lower() != 'n':
                herb = self.db.search_herb(view_details)
                if herb:
                    print(self.display_herb_details(herb))
        else:
            print(f"\nNo herbs found for benefit: {query}")

    def search_by_family(self) -> None:
        """Search herbs by plant family."""
        families = set(herb.family for herb in self.db.herbs.values())
        print("\nPlant families in database:")
        for i, family in enumerate(sorted(families), 1):
            print(f"{i}. {family}")
        
        query = input("\nEnter family name: ").strip()
        results = self.db.search_by_family(query)
        
        if results:
            print(f"\n✓ Found {len(results)} herb(s) in family '{query}':")
            for herb in results:
                print(f"  • {herb.name}")
        else:
            print(f"\nNo herbs found in family: {query}")

    def view_favorites(self) -> None:
        """Display favorite herbs."""
        if not self.favorites:
            print("\nNo favorites yet. Add some herbs to your favorites!")
            return
        
        print("\n" + "="*60)
        print("YOUR FAVORITE HERBS")
        print("="*60)
        print("\nReminder: Always consult a healthcare professional")
        print("before using any of these herbs.")
        print("="*60)
        for herb_name in self.favorites:
            herb = self.db.search_herb(herb_name)
            if herb:
                print(f"\n• {herb.name} ({herb.scientific_name})")
                print(f"  Benefits: {', '.join(herb.benefits[:2])}...")
                print(f"  ⚠️  Interactions: {', '.join(herb.interactions)}")

    def add_to_favorites(self) -> None:
        """Add herb to favorites."""
        herb_name = input("\nEnter herb name to add to favorites: ").strip()
        herb = self.db.search_herb(herb_name)
        
        if herb:
            if herb.name not in self.favorites:
                self.favorites.append(herb.name)
                self.save_favorites()
                print(f"\n✓ {herb.name} added to favorites!")
                print("⚠️  Remember to consult a healthcare professional before use.")
            else:
                print(f"\n{herb.name} is already in your favorites.")
        else:
            print(f"\nHerb '{herb_name}' not found.")


def main():
    """Entry point for the application."""
    app = HerbalApp()
    app.run()


if __name__ == "__main__":
    main()
