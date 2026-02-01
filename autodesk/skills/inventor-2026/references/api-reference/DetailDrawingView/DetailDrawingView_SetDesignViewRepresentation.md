# DetailDrawingView.SetDesignViewRepresentation Method

Parent Object: [DetailDrawingView](../DetailDrawingView/DetailDrawingView.md)

## Description

Method that sets a design view representation for a drawing view of an assembly. This method fails for drawing views of parts and presentations and in the case where the model (assembly) is unresolved.

## Syntax

DetailDrawingView.**SetDesignViewRepresentation**( ***Representation*** As String, [***Associative***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Representation | String | String that specifies the Design View Representation to set on the drawing view. The method returns a failure if a representation with this name is not found in the referenced assembly. |
| Associative | Boolean | Optional input Boolean that indicates whether to associatively apply the design view. If set to True, any changes to the design view in the referenced assembly will show in this view. If not specified, a value of False is used. |

## Version

Introduced in version 11
