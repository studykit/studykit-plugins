# BRepShell.wire Property

Parent Object: [BRepShell](BRepShell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepShell.h>

## Description

Returns the wire body, if any, that exists in this shell. Returns null if the shell doesn't have a wire body.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepShell\_var" is a variable referencing a BRepShell object. |

"bRepShell\_var" is a variable referencing a BRepShell object. ```` ``` #include <Fusion/BRep/BRepShell.h>  // Get the value of the property. Ptr<BRepWire> propertyValue = bRepShell_var->wire(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepWire](BRepWire.htm).

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |