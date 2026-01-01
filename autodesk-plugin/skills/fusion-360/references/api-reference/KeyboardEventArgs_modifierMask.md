# KeyboardEventArgs.modifierMask Property

Parent Object: [KeyboardEventArgs](KeyboardEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/KeyboardEventArgs.h>

## Description

Gets the set of keyboard modifiers that were active. The value is the Boolean combination of KeyboardModifiers values.

## Syntax

* [Python](#Python)
* [C++](#C++)

"keyboardEventArgs\_var" is a variable referencing a KeyboardEventArgs object. |

"keyboardEventArgs\_var" is a variable referencing a KeyboardEventArgs object. ```` ``` #include <Core/UserInterface/KeyboardEventArgs.h>  // Get the value of the property. integer propertyValue = keyboardEventArgs_var->modifierMask(); ``` ```` |

## Property Value

This is a read only property whose value is an integer.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |