# Generated by Django 5.0.2 on 2024-02-15 16:43

import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("content_manager", "0012_alter_contentpage_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contentpage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "hero",
                        wagtail.blocks.StructBlock(
                            [
                                ("bg_image", wagtail.images.blocks.ImageChooserBlock(label="Image d’arrière plan")),
                                (
                                    "bg_color",
                                    wagtail.blocks.RegexBlock(
                                        error_messages={
                                            "invalid": "La couleur n’est pas correcte, le format doit être #fff ou #f5f5fe"
                                        },
                                        label="Couleur d’arrière plan au format hexa (Ex: #f5f5fe)",
                                        regex="^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$",
                                        required=False,
                                    ),
                                ),
                                ("title", wagtail.blocks.CharBlock(label="Titre")),
                                ("text", wagtail.blocks.CharBlock(label="Texte", required=False)),
                                ("cta_label", wagtail.blocks.CharBlock(label="Texte du bouton", required=False)),
                                ("cta_link", wagtail.blocks.URLBlock(label="Lien du bouton", required=False)),
                                ("large", wagtail.blocks.BooleanBlock(label="Large", required=False)),
                                ("darken", wagtail.blocks.BooleanBlock(label="Assombrir", required=False)),
                            ],
                            label="Section promotionnelle",
                        ),
                    ),
                    (
                        "title",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(label="Titre")),
                                ("large", wagtail.blocks.BooleanBlock(label="Large", required=False)),
                            ],
                            label="Titre de page",
                        ),
                    ),
                    ("paragraph", wagtail.blocks.RichTextBlock(label="Texte avec mise en forme")),
                    ("paragraphlarge", wagtail.blocks.RichTextBlock(label="Texte avec mise en forme (large)")),
                    (
                        "image",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(label="Titre", required=False)),
                                ("image", wagtail.images.blocks.ImageChooserBlock(label="Illustration")),
                                (
                                    "alt",
                                    wagtail.blocks.CharBlock(
                                        label="Texte alternatif (description textuelle de l’image)", required=False
                                    ),
                                ),
                                ("caption", wagtail.blocks.CharBlock(label="Légende", required=False)),
                                ("url", wagtail.blocks.URLBlock(label="Lien", required=False)),
                            ]
                        ),
                    ),
                    (
                        "imageandtext",
                        wagtail.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock(label="Illustration (à gauche)")),
                                (
                                    "image_ratio",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[("3", "3/12"), ("5", "5/12"), ("6", "6/12")],
                                        label="Largeur de l’image",
                                    ),
                                ),
                                ("text", wagtail.blocks.RichTextBlock(label="Texte avec mise en forme (à droite)")),
                                (
                                    "link_label",
                                    wagtail.blocks.CharBlock(
                                        help_text="Le lien apparait en bas du bloc de droite, avec une flèche",
                                        label="Titre du lien",
                                        required=False,
                                    ),
                                ),
                                ("link_url", wagtail.blocks.URLBlock(label="Lien", required=False)),
                            ],
                            label="Bloc image à gauche et texte à droite",
                        ),
                    ),
                    (
                        "alert",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(label="Titre du message", required=False)),
                                ("description", wagtail.blocks.TextBlock(label="Texte du message", required=False)),
                                (
                                    "level",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("error", "Erreur"),
                                            ("success", "Succès"),
                                            ("info", "Information"),
                                            ("warning", "Attention"),
                                        ],
                                        label="Type de message",
                                    ),
                                ),
                                (
                                    "heading_tag",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("h2", "En-tête 2"),
                                            ("h3", "En-tête 3"),
                                            ("h4", "En-tête 4"),
                                            ("h5", "En-tête 5"),
                                            ("h6", "En-tête 6"),
                                            ("p", "Paragraphe"),
                                        ],
                                        help_text="À adapter à la structure de la page. Par défaut en-tête 3.",
                                        label="Niveau de titre",
                                    ),
                                ),
                            ],
                            label="Message d'alerte",
                        ),
                    ),
                    (
                        "callout",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(label="Titre de la mise en vant", required=False)),
                                ("text", wagtail.blocks.TextBlock(label="Texte mis en avant", required=False)),
                                (
                                    "heading_tag",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("h2", "En-tête 2"),
                                            ("h3", "En-tête 3"),
                                            ("h4", "En-tête 4"),
                                            ("h5", "En-tête 5"),
                                            ("h6", "En-tête 6"),
                                            ("p", "Paragraphe"),
                                        ],
                                        help_text="À adapter à la structure de la page. Par défaut en-tête 3.",
                                        label="Niveau de titre",
                                    ),
                                ),
                            ],
                            label="Texte mise en avant",
                        ),
                    ),
                    (
                        "quote",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        label="Illustration (à gauche)", required=False
                                    ),
                                ),
                                ("quote", wagtail.blocks.CharBlock(label="Citation")),
                                ("author_name", wagtail.blocks.CharBlock(label="Nom de l’auteur")),
                                ("author_title", wagtail.blocks.CharBlock(label="Titre de l’auteur")),
                            ],
                            label="Citation",
                        ),
                    ),
                    (
                        "video",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(label="Titre", required=False)),
                                ("caption", wagtail.blocks.CharBlock(label="Légende")),
                                (
                                    "url",
                                    wagtail.blocks.URLBlock(
                                        help_text="URL au format «\xa0embed\xa0» (Ex. : https://www.youtube.com/embed/gLzXOViPX-0)",
                                        label="Lien de la vidéo",
                                    ),
                                ),
                            ],
                            label="Vidéo",
                        ),
                    ),
                    (
                        "multicolumns",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "bg_image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        label="Image d’arrière plan", required=False
                                    ),
                                ),
                                (
                                    "bg_color",
                                    wagtail.blocks.RegexBlock(
                                        error_messages={
                                            "invalid": "La couleur n’est pas correcte, le format doit être #fff ou #f5f5fe"
                                        },
                                        label="Couleur d’arrière plan au format hexa (Ex: #f5f5fe)",
                                        regex="^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$",
                                        required=False,
                                    ),
                                ),
                                ("title", wagtail.blocks.CharBlock(label="Titre", required=False)),
                                (
                                    "columns",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            ("text", wagtail.blocks.RichTextBlock(label="Texte avec mise en forme")),
                                            (
                                                "image",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "title",
                                                            wagtail.blocks.CharBlock(label="Titre", required=False),
                                                        ),
                                                        (
                                                            "image",
                                                            wagtail.images.blocks.ImageChooserBlock(
                                                                label="Illustration"
                                                            ),
                                                        ),
                                                        (
                                                            "alt",
                                                            wagtail.blocks.CharBlock(
                                                                label="Texte alternatif (description textuelle de l’image)",
                                                                required=False,
                                                            ),
                                                        ),
                                                        (
                                                            "caption",
                                                            wagtail.blocks.CharBlock(label="Légende", required=False),
                                                        ),
                                                        ("url", wagtail.blocks.URLBlock(label="Lien", required=False)),
                                                    ],
                                                    label="Image",
                                                ),
                                            ),
                                            (
                                                "video",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "title",
                                                            wagtail.blocks.CharBlock(label="Titre", required=False),
                                                        ),
                                                        ("caption", wagtail.blocks.CharBlock(label="Légende")),
                                                        (
                                                            "url",
                                                            wagtail.blocks.URLBlock(
                                                                help_text="URL au format «\xa0embed\xa0» (Ex. : https://www.youtube.com/embed/gLzXOViPX-0)",
                                                                label="Lien de la vidéo",
                                                            ),
                                                        ),
                                                    ],
                                                    label="Vidéo",
                                                ),
                                            ),
                                            (
                                                "card",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        ("title", wagtail.blocks.CharBlock(label="Titre")),
                                                        ("description", wagtail.blocks.TextBlock(label="Texte")),
                                                        (
                                                            "image",
                                                            wagtail.images.blocks.ImageChooserBlock(label="Image"),
                                                        ),
                                                        ("url", wagtail.blocks.URLBlock(label="Lien", required=False)),
                                                        (
                                                            "document",
                                                            wagtail.documents.blocks.DocumentChooserBlock(
                                                                help_text="Sélectionnez un document pour rendre la carte cliquable vers celui ci (si le champ «\xa0Lien\xa0» n’est pas renseigné).",
                                                                label="ou Document",
                                                                required=False,
                                                            ),
                                                        ),
                                                    ],
                                                    label="Carte",
                                                ),
                                            ),
                                            (
                                                "quote",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "image",
                                                            wagtail.images.blocks.ImageChooserBlock(
                                                                label="Illustration (à gauche)", required=False
                                                            ),
                                                        ),
                                                        ("quote", wagtail.blocks.CharBlock(label="Citation")),
                                                        (
                                                            "author_name",
                                                            wagtail.blocks.CharBlock(label="Nom de l’auteur"),
                                                        ),
                                                        (
                                                            "author_title",
                                                            wagtail.blocks.CharBlock(label="Titre de l’auteur"),
                                                        ),
                                                    ],
                                                    label="Citation",
                                                ),
                                            ),
                                            (
                                                "text_cta",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "text",
                                                            wagtail.blocks.RichTextBlock(
                                                                label="Texte avec mise en forme", required=False
                                                            ),
                                                        ),
                                                        (
                                                            "cta_label",
                                                            wagtail.blocks.CharBlock(
                                                                help_text="Le lien apparait comme un bouton sous le bloc de texte",
                                                                label="Titre de l’appel à l’action",
                                                                required=False,
                                                            ),
                                                        ),
                                                        (
                                                            "cta_url",
                                                            wagtail.blocks.CharBlock(label="Lien", required=False),
                                                        ),
                                                    ],
                                                    label="Texte et appel à l’action",
                                                ),
                                            ),
                                            (
                                                "iframe",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "title",
                                                            wagtail.blocks.CharBlock(
                                                                help_text="Accessibilité : Le titre doit décrire, de façon claire et concise, le contenu embarqué.",
                                                                label="Titre",
                                                            ),
                                                        ),
                                                        (
                                                            "url",
                                                            wagtail.blocks.URLBlock(
                                                                help_text="Exemple pour Tally : https://tally.so/embed/w2jMRa",
                                                                label="Lien du cadre intégré",
                                                            ),
                                                        ),
                                                        (
                                                            "height",
                                                            wagtail.blocks.IntegerBlock(label="Hauteur en pixels"),
                                                        ),
                                                    ],
                                                    label="Cadre intégré",
                                                ),
                                            ),
                                        ],
                                        label="Multi-colonnes",
                                    ),
                                ),
                            ],
                            label="Multi-colonnes",
                        ),
                    ),
                    (
                        "accordions",
                        wagtail.blocks.StreamBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(label="Titre")),
                                (
                                    "accordion",
                                    wagtail.blocks.StructBlock(
                                        [
                                            ("title", wagtail.blocks.CharBlock(label="Titre")),
                                            ("content", wagtail.blocks.RichTextBlock(label="Contenu")),
                                        ],
                                        label="Accordéon",
                                        max_num=15,
                                        min_num=1,
                                    ),
                                ),
                            ],
                            label="Accordéons",
                        ),
                    ),
                    (
                        "stepper",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(label="Titre")),
                                ("total", wagtail.blocks.IntegerBlock(label="Nombre d’étapes")),
                                ("current", wagtail.blocks.IntegerBlock(label="Étape en cours")),
                                (
                                    "steps",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            (
                                                "step",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        ("title", wagtail.blocks.CharBlock(label="Titre de l’étape")),
                                                        ("detail", wagtail.blocks.TextBlock(label="Détail")),
                                                    ],
                                                    label="Étape",
                                                ),
                                            )
                                        ],
                                        label="Les étapes",
                                    ),
                                ),
                            ],
                            label="Étapes",
                        ),
                    ),
                    (
                        "separator",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "top_margin",
                                    wagtail.blocks.IntegerBlock(
                                        default=3, label="Espacement au dessus", max_value=15, min_value=0
                                    ),
                                ),
                                (
                                    "bottom_margin",
                                    wagtail.blocks.IntegerBlock(
                                        default=3, label="Espacement en dessous", max_value=15, min_value=0
                                    ),
                                ),
                            ],
                            label="Séparateur",
                        ),
                    ),
                    (
                        "html",
                        wagtail.blocks.RawHTMLBlock(
                            help_text="Avertissement : Utilisez le bloc HTML avec précaution.\n                Un code malveillant peut compromettre la sécurité du site.",
                            readonly=True,
                        ),
                    ),
                ],
                blank=True,
            ),
        ),
    ]
