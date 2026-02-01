# ConfigurationReplaceDesign.objectType Property

Parent Object: [ConfigurationReplaceDesign](ConfigurationReplaceDesign.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationReplaceDesign.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationReplaceDesign\_var" is a variable referencing a ConfigurationReplaceDesign object.  ```` ``` # Get the value of the property. propertyValue = configurationReplaceDesign_var.objectType ``` ```` |

"configurationReplaceDesign\_var" is a variable referencing a ConfigurationReplaceDesign object. ```` ``` #include <Fusion/Configurations/ConfigurationReplaceDesign.h>  // Get the value of the property. string propertyValue = configurationReplaceDesign_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |