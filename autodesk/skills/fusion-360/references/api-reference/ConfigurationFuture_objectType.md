# ConfigurationFuture.objectType Property

Parent Object: [ConfigurationFuture](ConfigurationFuture.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationFuture.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationFuture\_var" is a variable referencing a ConfigurationFuture object.  ```` ``` # Get the value of the property. propertyValue = configurationFuture_var.objectType ``` ```` |

"configurationFuture\_var" is a variable referencing a ConfigurationFuture object. ```` ``` #include <Fusion/Configurations/ConfigurationFuture.h>  // Get the value of the property. string propertyValue = configurationFuture_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |