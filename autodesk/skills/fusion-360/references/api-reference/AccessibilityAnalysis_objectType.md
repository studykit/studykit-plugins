# AccessibilityAnalysis.objectType Property

Parent Object: [AccessibilityAnalysis](AccessibilityAnalysis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/AccessibilityAnalysis.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"accessibilityAnalysis\_var" is a variable referencing an AccessibilityAnalysis object.  ```` ``` # Get the value of the property. propertyValue = accessibilityAnalysis_var.objectType ``` ```` |

"accessibilityAnalysis\_var" is a variable referencing an AccessibilityAnalysis object. ```` ``` #include <Fusion/Fusion/AccessibilityAnalysis.h>  // Get the value of the property. string propertyValue = accessibilityAnalysis_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |