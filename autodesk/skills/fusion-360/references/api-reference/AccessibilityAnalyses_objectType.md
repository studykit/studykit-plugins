# AccessibilityAnalyses.objectType Property

Parent Object: [AccessibilityAnalyses](AccessibilityAnalyses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/AccessibilityAnalyses.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"accessibilityAnalyses\_var" is a variable referencing an AccessibilityAnalyses object.  ```` ``` # Get the value of the property. propertyValue = accessibilityAnalyses_var.objectType ``` ```` |

"accessibilityAnalyses\_var" is a variable referencing an AccessibilityAnalyses object. ```` ``` #include <Fusion/Fusion/AccessibilityAnalyses.h>  // Get the value of the property. string propertyValue = accessibilityAnalyses_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |