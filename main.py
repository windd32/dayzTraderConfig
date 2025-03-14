#dayz_TraderConfig
import json

# Чтение данных из Loot.json
with open('Loot.json', 'r', encoding='utf-8') as f:
    loot_data = json.load(f)

# Чтение данных из TraderConfig.txt
with open('TraderConfig.txt', 'r', encoding='utf-8') as f:
    trader_config_lines = f.readlines()

# Создание нового списка для обновленных строк
updated_lines = []

# Проход по каждой строке TraderConfig.txt
for line in trader_config_lines:
    stripped_line = line.split('//')[0].strip()  # Убираем существующие комментарии и пробелы
    if stripped_line and not stripped_line.startswith('<'):  # Пропускаем строки с тегами
        item_class = stripped_line.split(',')[0].strip()
        if item_class in loot_data:
            comment = loot_data[item_class]
            updated_line = f"{line.rstrip()} // {comment}\n"
            updated_lines.append(updated_line)
            continue
    # Если нет совпадения или строка не нуждается в изменении, сохраняем её как есть
    updated_lines.append(line)

# Запись обновленных данных обратно в TraderConfig.txt
with open('TraderConfig_updated.txt', 'w', encoding='utf-8') as f:
    f.writelines(updated_lines)

print("Обновление завершено. Проверьте файл 'TraderConfig_updated.txt'.")
