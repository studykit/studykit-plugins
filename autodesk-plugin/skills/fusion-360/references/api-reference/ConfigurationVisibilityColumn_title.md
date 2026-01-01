# ConfigurationVisibilityColumn.title Property

Parent Object: [ConfigurationVisibilityColumn](ConfigurationVisibilityColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationVisibilityColumn.h>

## Description

The title of this column. In a top table, this can only be edited for suppression, visibility, parameter, and theme table columns. It behaves as read-only for all other types. In a theme table, the title of all the columns can be modified except for the column that represents the root component for materials and appearances.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationVisibilityColumn\_var" is a variable referencing a ConfigurationVisibilityColumn object.  ```` ``` # Get the value of the property. propertyValue = configurationVisibilityColumn_var.title  # Set the value of the property. configurationVisibilityColumn_var.title = propertyValue ``` ```` |

"configurationVisibilityColumn\_var" is a variable referencing a ConfigurationVisibilityColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationVisibilityColumn.h>  // Get the value of the property. string propertyValue = configurationVisibilityColumn_var->title();  // Set the value of the property, where value_var is a string. bool returnValue = configurationVisibilityColumn_var->title(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |