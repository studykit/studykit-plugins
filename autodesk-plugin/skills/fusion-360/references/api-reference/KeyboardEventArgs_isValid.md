# KeyboardEventArgs.isValid Property

Parent Object: [KeyboardEventArgs](KeyboardEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/KeyboardEventArgs.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"keyboardEventArgs\_var" is a variable referencing a KeyboardEventArgs object. |

"keyboardEventArgs\_var" is a variable referencing a KeyboardEventArgs object. ```` ``` #include <Core/UserInterface/KeyboardEventArgs.h>  // Get the value of the property. boolean propertyValue = keyboardEventArgs_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |