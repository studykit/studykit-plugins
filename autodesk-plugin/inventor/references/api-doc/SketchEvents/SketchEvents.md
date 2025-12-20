# SketchEvents Object

## Description

The SketchEvents object provides notification of sketch events including new, changed, solved or deleted sketches.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchEvents/SketchEvents_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Parent](../SketchEvents/SketchEvents_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../SketchEvents/SketchEvents_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnDelete](../SketchEvents/SketchEvents_OnDelete.md) | The OnDelete event notifies the client when a 2d or 3d sketch is being deleted. This notification is not sent when the contents of the sketch is deleted, but only when the sketch itself is deleted. |
| [OnNewSketch](../SketchEvents/SketchEvents_OnNewSketch.md) | Event that is fired whenever a sketch is created. |
| [OnNewSketch3D](../SketchEvents/SketchEvents_OnNewSketch3D.md) | The OnNewSketch3D event notifies the client when a new 3D sketch is being created. |
| [OnSketch3DChange](../SketchEvents/SketchEvents_OnSketch3DChange.md) | The OnSketch3DChange event notifies the client when the geometry of a 3D sketch is changed. |
| [OnSketchChange](../SketchEvents/SketchEvents_OnSketchChange.md) | The OnSketchChange event notifies the client when the geometry of a 2D sketch is changed. |

## Accessed From

[Application.SketchEvents](../Application/Application_SketchEvents.md), [InventorServer.SketchEvents](InventorServer_SketchEvents.md), [InventorServerObject.SketchEvents](InventorServerObject_SketchEvents.md)

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |