# CustomGraphicsLines.getOpacity Method

Parent Object: [CustomGraphicsLines](CustomGraphicsLines.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsLines.h>

## Description

Gets the opacity of the graphics entity.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsLines\_var" is a variable referencing a [CustomGraphicsLines](CustomGraphicsLines.htm) object. |

```` ```  #include <Fusion/Graphics/CustomGraphicsLines.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if getting the opacity information was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| opacity | double | The opacity value where 1.0 is completely opaque and 0.0 is completely transparent. |
| isOverride | boolean | Indicates if this entities opacity will override the opacity defined by the material. If true, it will override the material opacity and if false the opacity values will accumulate. |

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |