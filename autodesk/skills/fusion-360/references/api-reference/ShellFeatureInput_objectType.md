# ShellFeatureInput.objectType Property

Parent Object: [ShellFeatureInput](ShellFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ShellFeatureInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"shellFeatureInput\_var" is a variable referencing a ShellFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = shellFeatureInput_var.objectType ``` ```` |

"shellFeatureInput\_var" is a variable referencing a ShellFeatureInput object. ```` ``` #include <Fusion/Features/ShellFeatureInput.h>  // Get the value of the property. string propertyValue = shellFeatureInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |