# ListControlDefinition.listControlDisplayType Property

Parent Object: [ListControlDefinition](ListControlDefinition.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ListControlDefinition.h>

## Description

Gets how this list control will be displayed; as a standard list, a list of check boxes, or a list of radio buttons.

## Syntax

* [Python](#Python)
* [C++](#C++)

"listControlDefinition\_var" is a variable referencing a ListControlDefinition object. |

"listControlDefinition\_var" is a variable referencing a ListControlDefinition object. ```` ``` #include <Core/UserInterface/ListControlDefinition.h>  // Get the value of the property. ListControlDisplayTypes propertyValue = listControlDefinition_var->listControlDisplayType(); ``` ```` |

## Property Value

This is a read only property whose value is a [ListControlDisplayTypes](ListControlDisplayTypes.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |