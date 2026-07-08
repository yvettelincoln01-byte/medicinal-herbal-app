#!/usr/bin/env python3
"""
Medicinal Herbal App - Flask Web Version
A web-based application for browsing medicinal herbs with safety warnings.
"""

from flask import Flask, render_template, request, jsonify
import json
from typing import List, Dict, Optional
from dataclasses import dataclass
import os

app = Flask(__name__)


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

    def get_all_herbs(self) -> List[Herb]:
        """Get all herbs as list."""
        return sorted(self.herbs.values(), key=lambda h: h.name)

    def get_all_benefits(self) -> List[str]:
        """Get all unique benefits."""
        benefits = set()
        for herb in self.herbs.values():
            for benefit in herb.benefits:
                benefits.add(benefit)
        return sorted(list(benefits))

    def get_all_families(self) -> List[str]:
        """Get all unique plant families."""
        families = set(herb.family for herb in self.herbs.values())
        return sorted(list(families))


# Initialize database
db = HerbalDatabase()


@app.route('/')
def index():
    """Home page."""
    herbs = db.get_all_herbs()
    return render_template('index.html', herbs=herbs)


@app.route('/herb/<name>')
def view_herb(name):
    """View detailed information about a specific herb."""
    herb = db.search_herb(name)
    if not herb:
        return render_template('404.html', message=f"Herb '{name}' not found"), 404
    return render_template('herb.html', herb=herb)


@app.route('/search')
def search():
    """Search herbs by name, benefit, or family."""
    query = request.args.get('q', '').strip()
    search_type = request.args.get('type', 'name')  # name, benefit, or family
    
    results = []
    
    if search_type == 'benefit':
        results = db.search_by_benefit(query)
    elif search_type == 'family':
        results = db.search_by_family(query)
    else:  # name
        herb = db.search_herb(query)
        if herb:
            results = [herb]
    
    return render_template('search_results.html', query=query, results=results, search_type=search_type)


@app.route('/api/search')
def api_search():
    """API endpoint for search (returns JSON)."""
    query = request.args.get('q', '').strip()
    search_type = request.args.get('type', 'name')
    
    results = []
    
    if search_type == 'benefit':
        results = db.search_by_benefit(query)
    elif search_type == 'family':
        results = db.search_by_family(query)
    else:
        herb = db.search_herb(query)
        if herb:
            results = [herb]
    
    return jsonify({
        'query': query,
        'type': search_type,
        'count': len(results),
        'results': [{
            'name': h.name,
            'scientific_name': h.scientific_name,
            'family': h.family
        } for h in results]
    })


@app.route('/benefits')
def benefits():
    """Show all health benefits."""
    benefits_list = db.get_all_benefits()
    return render_template('benefits.html', benefits=benefits_list)


@app.route('/families')
def families():
    """Show all plant families."""
    families_list = db.get_all_families()
    return render_template('families.html', families=families_list)


@app.route('/about')
def about():
    """About page."""
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
