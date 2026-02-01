# ConfigurationParameterColumn.title Property

Parent Object: [ConfigurationParameterColumn](ConfigurationParameterColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationParameterColumn.h>

## Description

The title of this column. In a top table, this can only be edited for suppression, visibility, parameter, and theme table columns. It behaves as read-only for all other types. In a theme table, the title of all the columns can be modified except for the column that represents the root component for materials and appearances.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationParameterColumn\_var" is a variable referencing a ConfigurationParameterColumn object.  ```` ``` # Get the value of the property. propertyValue = configurationParameterColumn_var.title  # Set the value of the property. configurationParameterColumn_var.title = propertyValue ``` ```` |

"configurationParameterColumn\_var" is a variable referencing a ConfigurationParameterColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationParameterColumn.h>  // Get the value of the property. string propertyValue = configurationParameterColumn_var->title();  // Set the value of the property, where value_var is a string. bool returnValue = configurationParameterColumn_var->title(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |