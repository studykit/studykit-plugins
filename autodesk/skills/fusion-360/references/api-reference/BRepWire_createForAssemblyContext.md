# BRepWire.createForAssemblyContext Method

Parent Object: [BRepWire](BRepWire.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepWire.h>

## Description

Returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepWire\_var" is a variable referencing a [BRepWire](BRepWire.htm) object.```` ``` returnValue = bRepWire_var.createForAssemblyContext(occurrence) ``` ```` |

"bRepWire\_var" is a variable referencing a [BRepWire](BRepWire.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepWire](BRepWire.htm) | Returns the new BRepWire proxy or null if this isn't the NativeObject. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that defines the context for the created proxy. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [BrepWire Sample](BrepWireSample_Sample.htm) | BrepWires and BrepWire related functions |

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |