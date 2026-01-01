# ConfigurationReplaceDesigns.objectType Property

Parent Object: [ConfigurationReplaceDesigns](ConfigurationReplaceDesigns.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationReplaceDesigns.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationReplaceDesigns\_var" is a variable referencing a ConfigurationReplaceDesigns object.  ```` ``` # Get the value of the property. propertyValue = configurationReplaceDesigns_var.objectType ``` ```` |

"configurationReplaceDesigns\_var" is a variable referencing a ConfigurationReplaceDesigns object. ```` ``` #include <Fusion/Configurations/ConfigurationReplaceDesigns.h>  // Get the value of the property. string propertyValue = configurationReplaceDesigns_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |