# ConfigurationFeatureAspectStringCell.value Property

Parent Object: [ConfigurationFeatureAspectStringCell](ConfigurationFeatureAspectStringCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationFeatureAspectStringCell.h>

## Description

Gets and sets the value of the property associated with the parent column of this cell.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationFeatureAspectStringCell\_var" is a variable referencing a ConfigurationFeatureAspectStringCell object. |

"configurationFeatureAspectStringCell\_var" is a variable referencing a ConfigurationFeatureAspectStringCell object. ```` ``` #include <Fusion/Configurations/ConfigurationFeatureAspectStringCell.h>  // Get the value of the property. string propertyValue = configurationFeatureAspectStringCell_var->value();  // Set the value of the property, where value_var is a string. bool returnValue = configurationFeatureAspectStringCell_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |