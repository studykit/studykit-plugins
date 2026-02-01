# ConfigurationMaterialColumn.title Property

Parent Object: [ConfigurationMaterialColumn](ConfigurationMaterialColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationMaterialColumn.h>

## Description

The title of this column. In a top table, this can only be edited for suppression, visibility, parameter, and theme table columns. It behaves as read-only for all other types. In a theme table, the title of all the columns can be modified except for the column that represents the root component for materials and appearances.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationMaterialColumn\_var" is a variable referencing a ConfigurationMaterialColumn object.  ```` ``` # Get the value of the property. propertyValue = configurationMaterialColumn_var.title  # Set the value of the property. configurationMaterialColumn_var.title = propertyValue ``` ```` |

"configurationMaterialColumn\_var" is a variable referencing a ConfigurationMaterialColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationMaterialColumn.h>  // Get the value of the property. string propertyValue = configurationMaterialColumn_var->title();  // Set the value of the property, where value_var is a string. bool returnValue = configurationMaterialColumn_var->title(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |