# OnFaceCurve Object

## Description

OnFaceCurve Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLink](../OnFaceCurve/OnFaceCurve_BreakLink.md) | Method that breaks the link between the intersection curve and the model. |
| [Delete](../OnFaceCurve/OnFaceCurve_Delete.md) | Method that deletes the intersection curve. |
| [Edit](../OnFaceCurve/OnFaceCurve_Edit.md) | Method that edit the on face curve object. |
| [FitPoint](../OnFaceCurve/OnFaceCurve_FitPoint.md) | Read-only property that returns the fit point at the specified index. The indices correspond to the fit points in order from the start to the end of the splines in the curve. An Index of 1 returns the first SketchPoint3D. The FitPointCount property returns the. |
| [GetReferenceKey](../OnFaceCurve/OnFaceCurve_GetReferenceKey.md) | Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../OnFaceCurve/OnFaceCurve_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../OnFaceCurve/OnFaceCurve_AttributeSets.md) | Gets the Attribute Sets collection on this object. |
| [Closed](../OnFaceCurve/OnFaceCurve_Closed.md) | Read-write property that gets and sets whether the curve is closed. Set this to True may result to generate new splines in the curve to make the curve to be closed. Defining a curve to be closed will cause it to close and be periodic if possible at the closure. |
| [Constraints3D](../OnFaceCurve/OnFaceCurve_Constraints3D.md) | Read-only property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of geometric and bend constraints. |
| [ConstraintStatus](../OnFaceCurve/OnFaceCurve_ConstraintStatus.md) | Read-only property that returns an enum indicating the constraint status of the sketch entity, signifying whether it is fully constrained, over constrained, or under constrained. |
| [EndSketchPoint](../OnFaceCurve/OnFaceCurve_EndSketchPoint.md) | Read-only property that returns the SketchPoint3D that defines the position of the end of the curve. |
| [Faces](../OnFaceCurve/OnFaceCurve_Faces.md) | Read-only property that returns the NameValueMap object that contains the faces in sequence that the sketch splines on. |
| [FitPointCount](../OnFaceCurve/OnFaceCurve_FitPointCount.md) | Read-only property that returns the number of fit points for the curve. |
| [Name](../OnFaceCurve/OnFaceCurve_Name.md) | Read-write properrty that gets and sets name of the OnFaceCurve. When setting this property, the name must be unique with respect to all other OnFaceCurve objects in the document. If the name is not unique an error will occur. |
| [Parent](../OnFaceCurve/OnFaceCurve_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [RangeBox](../OnFaceCurve/OnFaceCurve_RangeBox.md) | Read-only property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [SketchEntities](../OnFaceCurve/OnFaceCurve_SketchEntities.md) | Read-only property that returns a collection of sketch entities that belong to the on face curve. |
| [StartSketchPoint](../OnFaceCurve/OnFaceCurve_StartSketchPoint.md) | Read-only property that returns the SketchPoint3D that defines the position of the start of the curve. |
| [Type](../OnFaceCurve/OnFaceCurve_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[OnFaceCurveProxy.NativeObject](../OnFaceCurveProxy/OnFaceCurveProxy_NativeObject.md), [OnFaceCurves.Add](../OnFaceCurves/OnFaceCurves_Add.md), [OnFaceCurves.Item](../OnFaceCurves/OnFaceCurves_Item.md)

## Derived Classes

[OnFaceCurveProxy](../OnFaceCurveProxy/OnFaceCurveProxy.md)

## Version

Introduced in version 2017
