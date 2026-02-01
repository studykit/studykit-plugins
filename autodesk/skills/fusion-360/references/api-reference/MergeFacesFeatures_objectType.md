# MergeFacesFeatures.objectType Property

Parent Object: [MergeFacesFeatures](MergeFacesFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MergeFacesFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mergeFacesFeatures\_var" is a variable referencing a MergeFacesFeatures object.  ```` ``` # Get the value of the property. propertyValue = mergeFacesFeatures_var.objectType ``` ```` |

"mergeFacesFeatures\_var" is a variable referencing a MergeFacesFeatures object. ```` ``` #include <Fusion/Features/MergeFacesFeatures.h>  // Get the value of the property. string propertyValue = mergeFacesFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |