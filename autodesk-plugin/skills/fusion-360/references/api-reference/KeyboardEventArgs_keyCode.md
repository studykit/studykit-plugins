# KeyboardEventArgs.keyCode Property

Parent Object: [KeyboardEventArgs](KeyboardEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/KeyboardEventArgs.h>

## Description

Gets the keyboard key.

## Syntax

* [Python](#Python)
* [C++](#C++)

"keyboardEventArgs\_var" is a variable referencing a KeyboardEventArgs object. |

"keyboardEventArgs\_var" is a variable referencing a KeyboardEventArgs object. ```` ``` #include <Core/UserInterface/KeyboardEventArgs.h>  // Get the value of the property. KeyCodes propertyValue = keyboardEventArgs_var->keyCode(); ``` ```` |

## Property Value

This is a read only property whose value is a [KeyCodes](KeyCodes.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |