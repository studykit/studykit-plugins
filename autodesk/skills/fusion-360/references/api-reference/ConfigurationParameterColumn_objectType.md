# ConfigurationParameterColumn.objectType Property

Parent Object: [ConfigurationParameterColumn](ConfigurationParameterColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationParameterColumn.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationParameterColumn\_var" is a variable referencing a ConfigurationParameterColumn object.  ```` ``` # Get the value of the property. propertyValue = configurationParameterColumn_var.objectType ``` ```` |

"configurationParameterColumn\_var" is a variable referencing a ConfigurationParameterColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationParameterColumn.h>  // Get the value of the property. string propertyValue = configurationParameterColumn_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |