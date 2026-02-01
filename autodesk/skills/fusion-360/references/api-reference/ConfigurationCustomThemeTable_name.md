# ConfigurationCustomThemeTable.name Property

Parent Object: [ConfigurationCustomThemeTable](ConfigurationCustomThemeTable.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationCustomThemeTable.h>

## Description

Gets and sets the name of the table as seen in the user interface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationCustomThemeTable\_var" is a variable referencing a ConfigurationCustomThemeTable object. |

"configurationCustomThemeTable\_var" is a variable referencing a ConfigurationCustomThemeTable object. ```` ``` #include <Fusion/Configurations/ConfigurationCustomThemeTable.h>  // Get the value of the property. string propertyValue = configurationCustomThemeTable_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = configurationCustomThemeTable_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |