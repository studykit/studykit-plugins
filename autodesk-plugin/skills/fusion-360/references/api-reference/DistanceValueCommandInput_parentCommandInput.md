# DistanceValueCommandInput.parentCommandInput Property

Parent Object: [DistanceValueCommandInput](DistanceValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/DistanceValueCommandInput.h>

## Description

Gets the parent CommandInput if this commandInput is the child of a TabCommandInput or GroupCommandInput. Returns null if there is no parent.

## Syntax

* [Python](#Python)
* [C++](#C++)

"distanceValueCommandInput\_var" is a variable referencing a DistanceValueCommandInput object. |

"distanceValueCommandInput\_var" is a variable referencing a DistanceValueCommandInput object. ```` ``` #include <Core/UserInterface/DistanceValueCommandInput.h>  // Get the value of the property. Ptr<CommandInput> propertyValue = distanceValueCommandInput_var->parentCommandInput(); ``` ```` |

## Property Value

This is a read only property whose value is a [CommandInput](CommandInput.htm).

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |