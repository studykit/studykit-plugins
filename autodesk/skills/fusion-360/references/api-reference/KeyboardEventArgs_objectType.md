# KeyboardEventArgs.objectType Property

Parent Object: [KeyboardEventArgs](KeyboardEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/KeyboardEventArgs.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"keyboardEventArgs\_var" is a variable referencing a KeyboardEventArgs object.  ```` ``` # Get the value of the property. propertyValue = keyboardEventArgs_var.objectType ``` ```` |

"keyboardEventArgs\_var" is a variable referencing a KeyboardEventArgs object. ```` ``` #include <Core/UserInterface/KeyboardEventArgs.h>  // Get the value of the property. string propertyValue = keyboardEventArgs_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |