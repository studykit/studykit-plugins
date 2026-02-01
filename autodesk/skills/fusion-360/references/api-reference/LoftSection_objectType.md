# LoftSection.objectType Property

Parent Object: [LoftSection](LoftSection.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftSection.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftSection\_var" is a variable referencing a LoftSection object.  ```` ``` # Get the value of the property. propertyValue = loftSection_var.objectType ``` ```` |

"loftSection\_var" is a variable referencing a LoftSection object. ```` ``` #include <Fusion/Features/LoftSection.h>  // Get the value of the property. string propertyValue = loftSection_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |