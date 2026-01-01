# MergeFacesFeatureInput.objectType Property

Parent Object: [MergeFacesFeatureInput](MergeFacesFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MergeFacesFeatureInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mergeFacesFeatureInput\_var" is a variable referencing a MergeFacesFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = mergeFacesFeatureInput_var.objectType ``` ```` |

"mergeFacesFeatureInput\_var" is a variable referencing a MergeFacesFeatureInput object. ```` ``` #include <Fusion/Features/MergeFacesFeatureInput.h>  // Get the value of the property. string propertyValue = mergeFacesFeatureInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |