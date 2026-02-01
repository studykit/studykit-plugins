# Toolbar.parentUserInterface Property

Parent Object: [Toolbar](Toolbar.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Toolbar.h>

## Description

Gets the owning UserInterface object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbar\_var" is a variable referencing a Toolbar object. |

"toolbar\_var" is a variable referencing a Toolbar object. ```` ``` #include <Core/UserInterface/Toolbar.h>  // Get the value of the property. Ptr<UserInterface> propertyValue = toolbar_var->parentUserInterface(); ``` ```` |

## Property Value

This is a read only property whose value is a [UserInterface](UserInterface.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |