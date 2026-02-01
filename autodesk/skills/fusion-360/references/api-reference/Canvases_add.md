# Canvases.add Method

Parent Object: [Canvases](Canvases.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/Canvases.h>

## Description

Creates a new canvas. Use the createInput method to first create an input object and set the available options. Then, pass that input object to the add method to create the canvas.

## Syntax

* [Python](#Python)
* [C++](#C++)

"canvases\_var" is a variable referencing a [Canvases](Canvases.htm) object.```` ``` returnValue = canvases_var.add(input) ``` ```` |

"canvases\_var" is a variable referencing a [Canvases](Canvases.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Canvas](Canvas.htm) | Returns the newly created Canvas object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [CanvasInput](CanvasInput.htm) | The CanvasInput object that defines the required information needed to create a new canvas. A CanvasInput object is the logical equivalent to the command dialog when creating a canvas. It provides access to the various options when creating a canvas. Calling the add method and passing in the CanvasInput is the equivalent to clicking the OK button on the dialog to create the canvas. |

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |