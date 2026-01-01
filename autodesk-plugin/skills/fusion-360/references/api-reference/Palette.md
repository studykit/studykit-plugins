# Palette Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Palette.h>

## Description

A Palette is a floating or docked dialog in Fusion. The browser is an example of a built-in palette. The contents of a custom palette are created by displaying an HTML file.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Palette_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](Palette_deleteMe.htm) | Deletes this palette. Fusion native palettes cannot be deleted. Use the isNative property to determine if this is a native or API created palette. |
| [sendInfoToHTML](Palette_sendInfoToHTML.htm) | Sends the string to the JavaScript associated with the loaded HTML. |
| [setMaximumSize](Palette_setMaximumSize.htm) | Sets the maximum size of the palette. The user cannot resize it to be larger than this size. This does not change the current size of the palette unless the palette is already larger than this size. |
| [setMinimumSize](Palette_setMinimumSize.htm) | Sets the minimum size of the palette. The user cannot resize it to be smaller than this size. This does not change the current size of the palette unless the palette is already smaller than this size.   Calling this method and setting the width and height to zero, removes the minimum size restriction. |
| [setPosition](Palette_setPosition.htm) | Sets the position of the palette. If the palette is docked or snapped, this will result in changing it to be floating. |
| [setSize](Palette_setSize.htm) | Sets the size of the palette. This is best used for a floating palette because either the width or height can be locked when a palette is docked. |
| [snapTo](Palette_snapTo.htm) | Snaps this palette to another palette. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [dockingOption](Palette_dockingOption.htm) | Defines the docking behavior for this palette. This controls how the user is allowed to dock the palette. |
| [dockingState](Palette_dockingState.htm) | Gets and sets how the palette is currently docked. |
| [height](Palette_height.htm) | Gets and sets the height of the palette. Setting this property may not always set the height. Depending on how the palette is docked or snapped, the height may not be editable. |
| [htmlFileURL](Palette_htmlFileURL.htm) | Gets and sets the URL to the HTML file that will be displayed in the palette. This can be a local file or a URL on the web where the HTML will be read. To avoid reading a file, this can also be the full HTML definition as a string.   If you are providing the HTML content as a string, it should begin with the  element. Any references made in the HTML should be to URL's and not local files since the local path is ambiguous. |
| [id](Palette_id.htm) | Gets The unique, language independent, ID of this palette. |
| [isNative](Palette_isNative.htm) | Indicates if this is one of the standard Fusion palettes or a custom palette created through the API. If true, it is a standard Fusion palette and will have some restrictions on changing its properties and cannot be deleted. |
| [isTransparent](Palette_isTransparent.htm) | Returns if this palette was created as a transparent palette. |
| [isValid](Palette_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](Palette_isVisible.htm) | Gets and sets whether this palette is currently being displayed in the user interface. |
| [left](Palette_left.htm) | Gets and sets the left side of the palette relative to screen space and in pixels. Because palettes can be positioned outside of the Fusion window, a value of zero indicates the left side of the screen and not the Fusion window. |
| [name](Palette_name.htm) | Gets and set the name of the palette as seen in the user interface. The name of native palettes cannot be set. |
| [objectType](Palette_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [top](Palette_top.htm) | Gets and sets the top of the palette relative to screen space and in pixels. Because palettes can be positioned outside of the Fusion window, a value of zero indicates the top of the screen and not the Fusion window. |
| [width](Palette_width.htm) | Gets and sets the width of the palette. Setting this property may not always set the width. Depending on how the palette is docked or snapped, the width may not be editable. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [closed](Palette_closed.htm) | This event is fired when the user clicks the "Close" button on the palette. You can choose if the "Close" button is available or not when you initially create the palette. When a palette is closed, it still exists but is change to invisible so you can still interact with it and retrieve any needed information and can make it visible again. Use the deleteMe method to delete the palette. |
| [incomingFromHTML](Palette_incomingFromHTML.htm) | This event is fired when the JavaScript associated with the HTML calls the adsk.fusionSendData function. This allows the HTML to communicate with the add-in by passing information to the add-in. |
| [navigatingURL](Palette_navigatingURL.htm) | This event is fired when a navigation event occurs on the page. This allows the add-in to determine how this navigation should be handled by the browser. |

## Accessed From

[Palettes.add](Palettes_add.htm), [Palettes.add2](Palettes_add2.htm), [Palettes.addTransparent](Palettes_addTransparent.htm), [Palettes.item](Palettes_item.htm), [Palettes.itemById](Palettes_itemById.htm)

## Derived Classes

[TextCommandPalette](TextCommandPalette.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Palette Sample](PaletteSample_Sample.htm) | Demonstrates how to create a palette, how to dock and snap palettes and how Fusion communicates with the palette HTML. The sample is an add-in. To use it, create a new Python add-in and replace the code with the code below. You also need to create an html file using the name and code below. The html file needs to be in the same folder as the py file.  When you load the add-in, you'll see two new commands under the ADD-INS panel of the TOOLS tab. The "Show Custom Palette" command will cause the custom palette to be displayed. It will remain displayed until you click its Close button. Clicking the "Click to send info to Fusion" button on the palette, will send information to your add-in, which uses the API to display that information in a message box. Running the "Send Info to HTML" command to send data to the javascript running in the palette, which uses it to update the content of a paragraph. palette.html  ``` <!DOCTYPE html> <html>     <head>     </head>     <body>         <p>Click the button below to send data to Fusion.</p>         <button type='button' onclick='sendInfoToFusion()'>Click to send info to Fusion</button>          <p id='p1'>Run the "Send Info to HTML" command in the ADD-INS panel to update this text.</p>         <br /><br /> 	     </body>     <script>         function sendInfoToFusion(){             var today = new Date();             var dd = String(today.getDate()).padStart(2, '0');             var mm = String(today.getMonth() + 1).padStart(2, '0');             var yyyy = today.getFullYear();              var hours = String(today.getHours()).padStart(2, '0');             var minutes = String(today.getMinutes()).padStart(2, '0');             var seconds = String(today.getSeconds()).padStart(2, '0');              var date = dd + '/' + mm + '/' + yyyy;             var time = hours + ':' + minutes + ':' + seconds;             var args = {                 arg1 : "Sample argument 1",                 arg2 : "Sample argument 2"             };             adsk.fusionSendData('send', JSON.stringify(args));         }                  window.fusionJavaScriptHandler = {handle: function(action, data){             try {                 if (action == 'send') { 					// Update a paragraph with the data passed in. 					document.getElementById('p1').innerHTML = data; 				} 				else if (action == 'debugger') {                     debugger; 				} 				else { 					return 'Unexpected command type: ' + action;                 }             } catch (e) {                 console.log(e);                 console.log('exception caught with command: ' + action + ', data: ' + data);             }             return 'OK';         }};     </script> </html> ``` |

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |