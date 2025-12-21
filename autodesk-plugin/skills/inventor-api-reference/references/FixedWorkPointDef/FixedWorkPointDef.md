# FixedWorkPointDef Object

## Description

Object that allows you to get and set the information that specifies a fixed work point.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FixedWorkPointDef/FixedWorkPointDef_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Parent](../FixedWorkPointDef/FixedWorkPointDef_Parent.md) | Property returning the parent WorkPoint object. |
| [Point](../FixedWorkPointDef/FixedWorkPointDef_Point.md) | Specifies the origin point of the work point. |
| [Type](../FixedWorkPointDef/FixedWorkPointDef_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [OnDrag Event - dragging a WorkPoint](../../sample-programs/UserInputEventsSink_OnDrag_Sample.md) | This sample demonstrates the use of the OnDrag event to drag fixed work points when no command is active. This sample only allows drags parallel to the X-Y plane. This sample is dependent on events and VB only supports events within a class module. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |