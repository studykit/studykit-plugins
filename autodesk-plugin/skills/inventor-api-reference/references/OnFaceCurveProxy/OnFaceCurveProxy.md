# OnFaceCurveProxy Object

Derived from: [OnFaceCurve](../OnFaceCurve/OnFaceCurve.md) Object

## Description

OnFaceCurveProxy Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLink](../OnFaceCurveProxy/OnFaceCurveProxy_BreakLink.md) | Method that breaks the link between the intersection curve and the model. |
| [Delete](../OnFaceCurveProxy/OnFaceCurveProxy_Delete.md) | Method that deletes the intersection curve. |
| [Edit](../OnFaceCurveProxy/OnFaceCurveProxy_Edit.md) | Method that edit the on face curve object. |
| [FitPoint](../OnFaceCurveProxy/OnFaceCurveProxy_FitPoint.md) | Read-only property that returns the fit point at the specified index. The indices correspond to the fit points in order from the start to the end of the splines in the curve. An Index of 1 returns the first SketchPoint3D. The FitPointCount property returns the. |
| [GetReferenceKey](../OnFaceCurveProxy/OnFaceCurveProxy_GetReferenceKey.md) | Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../OnFaceCurveProxy/OnFaceCurveProxy_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../OnFaceCurveProxy/OnFaceCurveProxy_AttributeSets.md) | Gets the Attribute Sets collection on this object. |
| [Closed](../OnFaceCurveProxy/OnFaceCurveProxy_Closed.md) | Read-write property that gets and sets whether the curve is closed. Set this to True may result to generate new splines in the curve to make the curve to be closed. Defining a curve to be closed will cause it to close and be periodic if possible at the closure. |
| [Constraints3D](../OnFaceCurveProxy/OnFaceCurveProxy_Constraints3D.md) | Read-only property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of geometric and bend constraints. |
| [ConstraintStatus](../OnFaceCurveProxy/OnFaceCurveProxy_ConstraintStatus.md) | Read-only property that returns an enum indicating the constraint status of the sketch entity, signifying whether it is fully constrained, over constrained, or under constrained. |
| [ContainingOccurrence](../OnFaceCurveProxy/OnFaceCurveProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [EndSketchPoint](../OnFaceCurveProxy/OnFaceCurveProxy_EndSketchPoint.md) | Read-only property that returns the SketchPoint3D that defines the position of the end of the curve. |
| [Faces](../OnFaceCurveProxy/OnFaceCurveProxy_Faces.md) | Read-only property that returns the NameValueMap object that contains the faces in sequence that the sketch splines on. |
| [FitPointCount](../OnFaceCurveProxy/OnFaceCurveProxy_FitPointCount.md) | Read-only property that returns the number of fit points for the curve. |
| [Name](../OnFaceCurveProxy/OnFaceCurveProxy_Name.md) | Read-write properrty that gets and sets name of the OnFaceCurve. When setting this property, the name must be unique with respect to all other OnFaceCurve objects in the document. If the name is not unique an error will occur. |
| [NativeObject](../OnFaceCurveProxy/OnFaceCurveProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../OnFaceCurveProxy/OnFaceCurveProxy_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [RangeBox](../OnFaceCurveProxy/OnFaceCurveProxy_RangeBox.md) | Read-only property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [SketchEntities](../OnFaceCurveProxy/OnFaceCurveProxy_SketchEntities.md) | Read-only property that returns a collection of sketch entities that belong to the on face curve. |
| [StartSketchPoint](../OnFaceCurveProxy/OnFaceCurveProxy_StartSketchPoint.md) | Read-only property that returns the SketchPoint3D that defines the position of the start of the curve. |
| [Type](../OnFaceCurveProxy/OnFaceCurveProxy_Type.md) | Gets the constant that indicates the type of this object. |

## Version

Introduced in version 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |