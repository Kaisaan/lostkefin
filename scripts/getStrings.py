import re
def find_japanese(text):
        japanese_pattern = re.compile(r'((?:[\u3000-\u303F\u3040-\u30ff\u4e00-\u9fff\u31F0-\u31FF\u3220-\u3243\u3280-\u337F]+|\[(?:GREEN|WHITE|RED|YELLOW|BLUE)\])+|\/\/POINTER[^\n]+|\[Adol|Dogi|Niena|Terra|Massea|Stein|Dorman|Rizze|Javil|Effey|King Kefin|Alga|Deios|Noties|Chase|Aisha|Wilee|Muhaba|Baruq|Abyss|Karion|Blacksmith|Sailor|Butler|Maid|Foot Soldier|Soldier|Adventurer A|Adventurer B|Merchant A|Merchant B|Kobold|Desert Old Woman|Desert Old Man|Desert Woman|Desert Man A|Desert Man B|Desert Girl|Desert Boy|Kefin Man A|Kefin Man B|Kefin Woman A|Kefin Woman B|Rebel A|Rebel B|Man A|Man B|Woman|Villager Man A|Villager Man B|Villager Girl A|Villager Girl B|Old Woman|Old Man|Boy A|Boy B|Girl A|Dog|Girl B|Kidnapped Stein|Noties & Deios|Beautiful Woman|Girl|Thug A|Thug B|Mysterious Voice|Mysterious Man|Big Man|Woman\])')
        return japanese_pattern.findall(text)

# this extracts all JP strings from a file and returns a CSV
with open("dump.txt", encoding="utf-8") as file:
	lines = file.read()
	matches = find_japanese(lines)
# print(matches)

with open("dump.tsv", "w", encoding="utf-8") as file:
        file.write("Pointer #,Speaker,Japanese\n")
        for line in matches:
                if line[0] == '/':
                        pointer_str = re.match(r'\/\/POINTER #(\d+)[^\n]+', line).group(1)
                elif re.match(r'[a-zA-Z]', line[0]):
                        speaker = line
                else:
                        file.write(f'{pointer_str},{speaker},{line}\n')