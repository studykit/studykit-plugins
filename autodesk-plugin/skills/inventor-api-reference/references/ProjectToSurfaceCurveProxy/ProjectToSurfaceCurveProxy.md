# ProjectToSurfaceCurveProxy Object

Derived from: [ProjectToSurfaceCurve](../ProjectToSurfaceCurve/ProjectToSurfaceCurve.md) Object

## Description

ProjectToSurfaceCurveProxy Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLink](../ProjectToSurfaceCurveProxy/ProjectToSurfaceCurveProxy_BreakLink.md) | Method that breaks the link between the project to surface curve and the model. This breaks the associativity to the model, allowing you to edit the individual sketch entities. |
| [Delete](../ProjectToSurfaceCurveProxy/ProjectToSurfaceCurveProxy_Delete.md) | Method that deletes the project to surface curve. This will delete all of the related sketch entities. |
| [Edit](../ProjectToSurfaceCurveProxy/ProjectToSurfaceCurveProxy_Edit.md) | Method that edits all of the inputs used to compute the project to surface curve. This method is more efficient than setting each of the individual properties since this will result in a single compute rather than computing after each property edit. |
| [GetReferenceKey](../ProjectToSurfaceCurveProxy/ProjectToSurfaceCurveProxy_GetReferenceKey.md) | Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ProjectToSurfaceCurveProxy/ProjectToSurfaceCurveProxy_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../ProjectToSurfaceCurveProxy/ProjectToSurfaceCurveProxy_AttributeSets.md) | Gets the Attribute Sets collection on this object. |
| [ContainingOccurrence](../ProjectToSurfaceCurveProxy/ProjectToSurfaceCurveProxy_ContainingOccurrence.md) | Use F1 key to display help topic. |
| [Curves](../ProjectToSurfaceCurveProxy/ProjectToSurfaceCurveProxy_Curves.md) | Read-write property that gets and sets the sketch curves to project. Valid objects are 2D&3D sketch entities. |
| [Faces](../ProjectToSurfaceCurveProxy/ProjectToSurfaceCurveProxy_Faces.md) | Read-write property that defines the surfaces to project sketch curves to. The collection can contain Face and WorkPlane objects. |
| [Name](../ProjectToSurfaceCurveProxy/ProjectToSurfaceCurveProxy_Name.md) | Property that gets and sets name of the project to surface curve. When setting this property, the name must be unique with respect to all other project to surface curves in the document. If the name is not unique an error will occur. |
| [NativeObject](../ProjectToSurfaceCurveProxy/ProjectToSurfaceCurveProxy_NativeObject.md) | Use F1 key to display help topic. |
| [Parent](../ProjectToSurfaceCurveProxy/ProjectToSurfaceCurveProxy_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [ProjectDirection](../ProjectToSurfaceCurveProxy/ProjectToSurfaceCurveProxy_ProjectDirection.md) | Read-write property that defines the project direction. The direction is bidirectional. If the ProjectionType is not kProjectAlongVectorType setting this property will fail. If the ProjectionType is kProjectAlongVectorType, set this to Nothing to use the norma. |
| [ProjectionType](../ProjectToSurfaceCurveProxy/ProjectToSurfaceCurveProxy_ProjectionType.md) | Read-write property that defines the projection type for project to surface curve. Set this from other value to kProjectAlongVectorType will fail, the Edit function can be used to change the ProjectionType and ProjectDirection. |
| [SketchEntities](../ProjectToSurfaceCurveProxy/ProjectToSurfaceCurveProxy_SketchEntities.md) | Read-only property that returns a collection of sketch entities that belong to the project to surface curve. The sketch entities returned by this property cannot be edited or deleted because they are associated with the project to surface curve in the model. T. |
| [Type](../ProjectToSurfaceCurveProxy/ProjectToSurfaceCurveProxy_Type.md) | Gets the constant that indicates the type of this object. |

## Version

Introduced in version 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |