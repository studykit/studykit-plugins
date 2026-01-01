# InputChangedEventArgs.objectType Property

Parent Object: [InputChangedEventArgs](InputChangedEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/InputChangedEventArgs.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"inputChangedEventArgs\_var" is a variable referencing an InputChangedEventArgs object.  ```` ``` # Get the value of the property. propertyValue = inputChangedEventArgs_var.objectType ``` ```` |

"inputChangedEventArgs\_var" is a variable referencing an InputChangedEventArgs object. ```` ``` #include <Core/UserInterface/InputChangedEventArgs.h>  // Get the value of the property. string propertyValue = inputChangedEventArgs_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |