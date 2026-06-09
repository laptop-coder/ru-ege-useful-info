from jinja2 import Template

ru_ege_info_message_template = Template(
        """{{date}}\n\n1. Орфоэпия:\n{{orthoepy}}\n\n2. Паронимы:\n{{paronyms}}\n\n3. Фразеологизм:\n{{phraseological_unit}}\n\n4. Безударные в корне:\n{{unstressed_at_root}}"""
)
