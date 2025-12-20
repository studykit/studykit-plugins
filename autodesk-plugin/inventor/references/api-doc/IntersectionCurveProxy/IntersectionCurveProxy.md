# IntersectionCurveProxy Object

Derived from: [IntersectionCurve](../IntersectionCurve/IntersectionCurve.md) Object

## Description

Represent a part IntersectionCurveProxy object within an assembly.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLink](../IntersectionCurveProxy/IntersectionCurveProxy_BreakLink.md) | Method that breaks the link between the intersection curve and the model. This breaks the associativity to the model, allowing you to edit the individual sketch entities. |
| [Delete](../IntersectionCurveProxy/IntersectionCurveProxy_Delete.md) | Method that deletes the intersection curve. This will delete all of the related sketch entities. |
| [Edit](../IntersectionCurveProxy/IntersectionCurveProxy_Edit.md) | Method that edits all of the inputs used to compute the intersection curve. This method is more efficient than setting each of the individual properties since this will result in a single compute rather than computing after each property edit. |
| [GetReferenceKey](../IntersectionCurveProxy/IntersectionCurveProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../IntersectionCurveProxy/IntersectionCurveProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../IntersectionCurveProxy/IntersectionCurveProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../IntersectionCurveProxy/IntersectionCurveProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [EntityOne](../IntersectionCurveProxy/IntersectionCurveProxy_EntityOne.md) | Read-write property that defines the first entity involved in the intersection. |
| [EntityTwo](../IntersectionCurveProxy/IntersectionCurveProxy_EntityTwo.md) | Read-write property that defines the second entity(s) involved in the intersection. |
| [Name](../IntersectionCurveProxy/IntersectionCurveProxy_Name.md) | Property that gets and sets name of the intersection curve. |
| [NativeObject](../IntersectionCurveProxy/IntersectionCurveProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../IntersectionCurveProxy/IntersectionCurveProxy_Parent.md) | Read-only property that returns the parent 3D sketch of the intersection curve. |
| [SketchEntities](../IntersectionCurveProxy/IntersectionCurveProxy_SketchEntities.md) | Read-only property that returns a collection of sketch entities that belong to the intersection curve. The sketch entities returned by this property cannot be edited or deleted because they are associated with the intersection curve in the model. The BreakLink method can be used to break this association so they are individually editable. |
| [Type](../IntersectionCurveProxy/IntersectionCurveProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |