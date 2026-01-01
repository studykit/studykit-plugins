# ImageCommandInput.parentCommandInput Property

Parent Object: [ImageCommandInput](ImageCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ImageCommandInput.h>

## Description

Gets the parent CommandInput if this commandInput is the child of a TabCommandInput or GroupCommandInput. Returns null if there is no parent.

## Syntax

* [Python](#Python)
* [C++](#C++)

"imageCommandInput\_var" is a variable referencing an ImageCommandInput object. |

"imageCommandInput\_var" is a variable referencing an ImageCommandInput object. ```` ``` #include <Core/UserInterface/ImageCommandInput.h>  // Get the value of the property. Ptr<CommandInput> propertyValue = imageCommandInput_var->parentCommandInput(); ``` ```` |

## Property Value

This is a read only property whose value is a [CommandInput](CommandInput.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |