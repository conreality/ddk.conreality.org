Video Camera
============

.. code-block:: ocaml

   (* Device driver interface for cameras. *)
   module Camera : sig
     class virtual interface : object
       inherit Device.interface
       (* Device interface: *)
       method reset : unit
       method parent : Device.t option
       method is_privileged : bool
       method virtual driver_name : string
       method virtual device_name : string
       method device_path : string list
       (* Camera interface: *)
       method virtual init :unit
       method virtual close : unit
     end
     type t = interface
   end
