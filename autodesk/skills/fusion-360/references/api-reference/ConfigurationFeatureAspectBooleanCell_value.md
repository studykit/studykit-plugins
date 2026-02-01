# ConfigurationFeatureAspectBooleanCell.value Property

Parent Object: [ConfigurationFeatureAspectBooleanCell](ConfigurationFeatureAspectBooleanCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationFeatureAspectBooleanCell.h>

## Description

Gets and sets the value of the property associated with the parent column of this cell.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationFeatureAspectBooleanCell\_var" is a variable referencing a ConfigurationFeatureAspectBooleanCell object. |

"configurationFeatureAspectBooleanCell\_var" is a variable referencing a ConfigurationFeatureAspectBooleanCell object. ```` ``` #include <Fusion/Configurations/ConfigurationFeatureAspectBooleanCell.h>  // Get the value of the property. boolean propertyValue = configurationFeatureAspectBooleanCell_var->value();  // Set the value of the property, where value_var is a boolean. bool returnValue = configurationFeatureAspectBooleanCell_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |