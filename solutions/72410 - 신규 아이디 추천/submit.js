const solution = new_id =>
    new_id.toLowerCase()
          .replace(/[^\w-_.]/g, "")
          .replace(/\.+/g, ".")
          .replace(/^\.|\.$/g, "")
          .replace(/^$/, "a")
          .match(/^.{0,14}[^.]/)[0]
          .replace(/^(.)$/, "$1$1$1")
          .replace(/^(.)(.)$/, "$1$2$2");
