# ActiveSelectionEventArgs.objectType Property

Parent Object: [ActiveSelectionEventArgs](ActiveSelectionEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ActiveSelectionEventArgs.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"activeSelectionEventArgs\_var" is a variable referencing an ActiveSelectionEventArgs object.  ```` ``` # Get the value of the property. propertyValue = activeSelectionEventArgs_var.objectType ``` ```` |

"activeSelectionEventArgs\_var" is a variable referencing an ActiveSelectionEventArgs object. ```` ``` #include <Core/UserInterface/ActiveSelectionEventArgs.h>  // Get the value of the property. string propertyValue = activeSelectionEventArgs_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |