# ImageCommandInput.parentCommand Property

Parent Object: [ImageCommandInput](ImageCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ImageCommandInput.h>

## Description

Gets the parent Command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"imageCommandInput\_var" is a variable referencing an ImageCommandInput object. |

"imageCommandInput\_var" is a variable referencing an ImageCommandInput object. ```` ``` #include <Core/UserInterface/ImageCommandInput.h>  // Get the value of the property. Ptr<Command> propertyValue = imageCommandInput_var->parentCommand(); ``` ```` |

## Property Value

This is a read only property whose value is a [Command](Command.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |