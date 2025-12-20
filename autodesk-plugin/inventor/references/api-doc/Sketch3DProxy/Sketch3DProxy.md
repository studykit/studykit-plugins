# Sketch3DProxy Object

Derived from: [Sketch3D](../Sketch3D/Sketch3D.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../Sketch3DProxy/Sketch3DProxy_Delete.md) | Method that deletes the 3D sketch. This method will fail in the cases where the sketch is active, and when there are dependents on the sketch. In the cases where other geometry, besides a feature, is dependent on the sketch, the dependent geometry will be deleted or modified. |
| [Edit](../Sketch3DProxy/Sketch3DProxy_Edit.md) | Method that causes the Sketch environment to be invoked with this sketch available for interactive edit. |
| [ExitEdit](../Sketch3DProxy/Sketch3DProxy_ExitEdit.md) | Method that causes the Sketch environment to be closed and the user interface to return to the previous environment. This is equivalent to the Return command. This method is only valid in the case where this sketch is open for edit within the user interface. Calling this method in other cases will not do anything. |
| [GetReferenceKey](../Sketch3DProxy/Sketch3DProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [Include](../Sketch3DProxy/Sketch3DProxy_Include.md) | Method that creates a new sketch entity by copying other entities into the sketch. |
| [SetEndOfPart](../Sketch3DProxy/Sketch3DProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. The argument defines if the end-of-part marker will be positioned just before or just after the object. If the object is contained within another object and is not in the top level of the browser, the positioning of the marker will be relative to the top-level object the calling object is contained within. An example of this case is a sketch that has not been shared and has been consumed by a feature. Another example is a nested work feature. |
| [Solve](../Sketch3DProxy/Sketch3DProxy_Solve.md) | Method that causes the sketch to solve. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../Sketch3DProxy/Sketch3DProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../Sketch3DProxy/Sketch3DProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CheckSumValue](../Sketch3DProxy/Sketch3DProxy_CheckSumValue.md) | Gets sketch checksum value. |
| [Consumed](../Sketch3DProxy/Sketch3DProxy_Consumed.md) | Gets whether the 3D Sketch is consumed or not. |
| [ContainingOccurrence](../Sketch3DProxy/Sketch3DProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [DeferUpdates](../Sketch3DProxy/Sketch3DProxy_DeferUpdates.md) | Gets and sets whether to defer the solving of the sketch. |
| [Dependents](../Sketch3DProxy/Sketch3DProxy_Dependents.md) | Property that returns a collection of the objects that are dependent on the 3D sketch. Examples of objects that can be returned are profiles, features, work features, other sketches, and assembly constraints. |
| [DimensionConstraints3D](../Sketch3DProxy/Sketch3DProxy_DimensionConstraints3D.md) | Property that returns a collection of all dimension constraints on the 3D sketch. |
| [DimensionsVisible](../Sketch3DProxy/Sketch3DProxy_DimensionsVisible.md) | Gets and sets whether the dimensions on the sketch are visible. |
| [DisabledActionTypes](../Sketch3DProxy/Sketch3DProxy_DisabledActionTypes.md) | Gets and sets the action types valid for this sketch. |
| [Exported](../Sketch3DProxy/Sketch3DProxy_Exported.md) | Read-write property that gets and sets whether the object is exported. Objects must be marked for export in order for them to be derived. |
| [GeometricConstraints3D](../Sketch3DProxy/Sketch3DProxy_GeometricConstraints3D.md) | Property that returns a collection of all geometric constraints on the 3D sketch. |
| [HasReferenceComponent](../Sketch3DProxy/Sketch3DProxy_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [HealthStatus](../Sketch3DProxy/Sketch3DProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [HelicalCurves](../Sketch3DProxy/Sketch3DProxy_HelicalCurves.md) | Gets the HelicalCurves collection object. |
| [IntersectionCurves](../Sketch3DProxy/Sketch3DProxy_IntersectionCurves.md) | Read-only property that returns the IntersectionCurves collection object. This collection provides access to the existing intersection curves in the sketch and provides functionality to create new intersection curves. |
| [IsOwnedByFeature](../Sketch3DProxy/Sketch3DProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../Sketch3DProxy/Sketch3DProxy_Name.md) | Gets and sets name of the 3D sketch. |
| [NativeObject](../Sketch3DProxy/Sketch3DProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OnFaceCurves](../Sketch3DProxy/Sketch3DProxy_OnFaceCurves.md) | Gets the 3D Sketch OnFaceCurves collection Object. |
| [OverrideColor](../Sketch3DProxy/Sketch3DProxy_OverrideColor.md) | Specifies the override color, if any, for this sketch. |
| [OwnedBy](../Sketch3DProxy/Sketch3DProxy_OwnedBy.md) | Read-only property that returns the client feature that owns this object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parent](../Sketch3DProxy/Sketch3DProxy_Parent.md) | Property that returns the parent of the object. This will return the parent PartComponentDefinition. |
| [Profiles3D](../Sketch3DProxy/Sketch3DProxy_Profiles3D.md) | Property that returns the Profiles3D collection object. |
| [ProjectToSurfaceCurves](../Sketch3DProxy/Sketch3DProxy_ProjectToSurfaceCurves.md) | Read-only property that returns the ProjectToSurfaceCurves collection object. This object provides access to all the existing ProjectToSurfaceCurve objects in the sketch and also provides methods to create new ProjectToSurfaceCurve objects. |
| [ReferenceComponent](../Sketch3DProxy/Sketch3DProxy_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../Sketch3DProxy/Sketch3DProxy_ReferencedEntity.md) | Property that returns the referenced 3D sketch, if there is one. Currently this property always returns 'Nothing'; it was implemented to support future functionality. |
| [Shared](../Sketch3DProxy/Sketch3DProxy_Shared.md) | Gets and sets whether the sketch is shared or not. |
| [SilhouetteCurves](../Sketch3DProxy/Sketch3DProxy_SilhouetteCurves.md) | Gets the SilhouetteCurve collection Object. |
| [SketchArcs3D](../Sketch3DProxy/Sketch3DProxy_SketchArcs3D.md) | Property that returns the SketchArcs3D collection object. This collection provides access to the existing arcs and bends in the sketch and provides functionality to create new bends. |
| [SketchCircles3D](../Sketch3DProxy/Sketch3DProxy_SketchCircles3D.md) | Property that returns the SketchCircles3D collection object. This collection provides access to the existing circles in the sketch. |
| [SketchControlPointSplines3D](../Sketch3DProxy/Sketch3DProxy_SketchControlPointSplines3D.md) | Read-only property that returns the SketchControlPointSplines3D collection object. This collection provides access to the existing control point splines in the sketch and provides functionality to create new control point curves. |
| [SketchEllipses3D](../Sketch3DProxy/Sketch3DProxy_SketchEllipses3D.md) | Property that returns the SketchEllipses3D collection object. This collection provides access to the existing ellipses in the sketch. |
| [SketchEllipticalArcs3D](../Sketch3DProxy/Sketch3DProxy_SketchEllipticalArcs3D.md) | Property that returns the SketchEllipticalArcs3D collection object. This collection provides access to the existing elliptical arcs in the sketch. |
| [SketchEntities3D](../Sketch3DProxy/Sketch3DProxy_SketchEntities3D.md) | Property that returns a collection of all geometric entities on the sketch, regardless of their type. |
| [SketchEquationCurves3D](../Sketch3DProxy/Sketch3DProxy_SketchEquationCurves3D.md) | Read-only property that returns the SketchEquationCurves3D collection object. This collection provides access to the existing equation curves in the sketch and provides functionality to create new equation curves. |
| [SketchFixedSplines3D](../Sketch3DProxy/Sketch3DProxy_SketchFixedSplines3D.md) | Property that gets the collection object. |
| [SketchLines3D](../Sketch3DProxy/Sketch3DProxy_SketchLines3D.md) | Property that returns the SketchLines3D collection object. This collection provides access to the existing lines in the sketch and provides functionality to create new lines. |
| [SketchPoints3D](../Sketch3DProxy/Sketch3DProxy_SketchPoints3D.md) | Property that returns the SketchPoints3D collection object. This collection provides access to the existing points in the sketch. |
| [SketchSplines3D](../Sketch3DProxy/Sketch3DProxy_SketchSplines3D.md) | Property that returns the SketchSplines3D collection object. This collection provides access to the existing splines in the sketch. |
| [Type](../Sketch3DProxy/Sketch3DProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../Sketch3DProxy/Sketch3DProxy_Visible.md) | Gets and sets the visibility of the sketch. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |